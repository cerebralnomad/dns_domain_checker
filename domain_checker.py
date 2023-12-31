#! /usr/bin/env python3

'''
Script to check the availability of domain names.
Domain names to be checked can be added as command line arguments:
        domain_checker.py example.com example2.com

Or they can be read from a file:
        domain_checker.py --list domain_list.txt

When using an external file, put one domain per line. 
'''

import argparse
import whois
import datetime

def main():
    
    parser = argparse.ArgumentParser(
            formatter_class = argparse.RawDescriptionHelpFormatter,
            description = 'Check the availability of one or more domain names',
            prog = 'DomainChecker',
            usage = 'domain_checker.py DOMAIN_NAME DOMAIN_NAME',
            epilog = ('''\
examples:

    Domain names can be added as command line arguments:

        domain_checker.py example1.com example2.com

    Or they can be read from an external file:
            
        domain_checker.py --list domain_list.txt

    When using an external file, put one domain per line.

    To get more information in addition to the availability and expiration,
    use the details option (-d, --details)
    This flag can be used with both command line arguments and an external 
    list of domains:

        domain_checker.py -d -l domain_list.txt
        domain_checker.py --details <example.com> <example2.com>
                     ''')
                     )

    parser.add_argument('domain', nargs='*', help='Domain names to be checked')
    parser.add_argument('-l', '--list', help='List of domains to process')
    parser.add_argument('-d', '--details', action='store_true', help='Return more details of each domain')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.9')

    args = parser.parse_args()

    if args.list and not args.details:
            domainfile = args.list
            check_from_file(domainfile)
    elif args.list and args.details:
            domainfile = args.list
            check_details_from_file(domainfile)
    elif args.details and not args.list:
            detailed_domain_check(args)
    else:
            domain_check(args)

def domain_check(args):

    for domain in args.domain:
            
        try:
            w = whois.whois(domain)
            
            print(domain + " is not available. Expiry date: " + str(w.expiration_date))
                
        except whois.parser.PywhoisError:
            print(domain + " is available")
        except:
            print("Error: Invalid domain name or unable to connect to WHOIS server.")

def detailed_domain_check(args):
        
        for domain in args.domain:

            try:

                w = whois.whois(domain)
                domain_name = domain
                registrar = w.registrar
                created = w.creation_date
                updated = w.updated_date
                expiry = w.expiration_date
                server = w.whois_server
                name_serv = w.name_servers[0]
                reg_name = w.name
                reg_org = w.org
                days_left = (expiry-datetime.datetime.now()).days
                
                print(domain_name + " is not available.")
                print("")
                print('Domain: ' + domain_name)
                print('Registrar: ' + registrar)
                print('Created: ' + str(created))
                print('Updated: ' + str(updated))
                print('Expires: ' + str(expiry))
                print('Time Remaining: ' + str(days_left) + ' days')
                print('Whois Server: ' + server)
                print('Name Server: ' + name_serv)
                print('Registrant: ' + str(reg_name))
                print('Orgnization: ' + str(reg_org))
                print("")

            except whois.parser.PywhoisError:
                    print(domain + ' is available')
            except:
                    print("Error: Invalid domain name or unable to connect to WHOIS server.")

                                
def check_from_file(domainfile):

        with open(domainfile, 'r') as list_of_domains:
                for line in list_of_domains:
                        domain = line.strip()
                        try:
                                w = whois.whois(domain)
                                print(domain + " is not available. Expiry date: " + str(w.expiration_date))
                            
                        except whois.parser.PywhoisError:
                                print(domain + " is available")
                        except:
                                print("Error: Invalid domain name or unable to connect to WHOIS server.")

def check_details_from_file(domainfile):

        with open(domainfile, 'r') as list_of_domains:
                for line in list_of_domains:
                        domain = line.strip()
                        try:
                                w = whois.whois(domain)
                                domain_name = domain
                                registrar = w.registrar
                                created = w.creation_date
                                updated = w.updated_date
                                expiry = w.expiration_date
                                server = w.whois_server
                                name_serv = w.name_servers[0]
                                reg_name = w.name
                                reg_org = w.org
                                days_left = (expiry-datetime.datetime.now()).days
                                
                                print(domain + " is not available.")
                                print("")
                                print('Domain: ' + domain_name)
                                print('Registrar: ' + registrar)
                                print('Created: ' + str(created))
                                print('Updated: ' + str(updated))
                                print('Expires: ' + str(expiry))
                                print('Time Remaining: ' + str(days_left) + ' days') 
                                print('Whois Server: ' + server)
                                print('Name Server: ' + name_serv)
                                print('Registrant: ' + str(reg_name))
                                print('Orgnization: ' + str(reg_org))
                                print("")

                        except whois.parser.PywhoisError:
                                print(domain + ' is available.')
                        except:
                                print("Error: Invalid domain name or unable to connect to WHOIS server.")

main()

