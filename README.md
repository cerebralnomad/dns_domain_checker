# Domain Name Availability Checker

A simple CLI script to check whether a domain name is available and to optionally return additional information about domains which are already registered.
Written in Python 3

## Requires python-whois module

    pip install python-whois


## Usage

    domain_checker.py [option] [domain] [domain]


positional arguments:

    domain          domain name(s) to be checked. Required unless using an external list of names.

optional arguments:

    -l,  --list     use an external file containing a list of domain names

    -d, --details   return additonal information from the WHOIS server for each domain name

examples:

    domain_checker.py example.com - perform availability check on example.com
    domain_checker.py -d example.com - check example.com and return additional details 
    domain_checker.py -l domain_names.txt - process list of names from external file
    domain_checker.py -d -l domain_names.txt - use external file and return mroe details

    $ domain_checker.py pepsi.com
    pepsi.com is not available. Expiry date: 2024-01-13 05:00:00

    $ domain_checker.py -d pepsi.com
    pepsi.com is not available.

    Domain: pepsi.com
    Registrar: CSC CORPORATE DOMAINS, INC.
    Created: [datetime.datetime(1993, 1, 14, 5, 0), datetime.datetime(1993, 1, 14, 0, 0)]
    Updated: [datetime.datetime(2022, 1, 9, 6, 11, 55), datetime.datetime(2022, 1, 9, 1, 11, 55)]
    Expires: 2024-01-13 05:00:00
    Whois Server: whois.corporatedomains.com
    Name Server: NS1.PBSG.COM
    Registrant: NO DATA
    Orgnization: PepsiCo, Inc   

    $ domain_checker.py  pepsi.com mountaindew.com
    pepsi.com is not available. Expiry date: 2024-01-13 05:00:00
    mountaindew.com is not available. Expiry date: 2023-12-21 05:00:00

    $ domain_checker.py -l domain_list.txt
    wired.com is not available. Expiry date: 2023-11-19 05:00:00
    arstechnia.com is not available. Expiry date: 2023-12-07 05:45:00
    made_up_domain.com is available

    $ domain_checker.py -d -l domain_list.txt
     wired.com is not available.

     Domain: wired.com
     Registrar: CSC CORPORATE DOMAINS, INC.
     Created: [datetime.datetime(1992, 11, 20, 5, 0), datetime.datetime(1992, 11, 20, 0, 0)]
     Updated: [datetime.datetime(2023, 2, 20, 13, 49, 21), datetime.datetime(2023, 2, 16, 13, 38, 9)]
     Expires: 2023-11-19 05:00:00
     Whois Server: whois.corporatedomains.com
     Name Server: NS-1116.AWSDNS-11.ORG
     Registrant: Domain Administrator
     Orgnization: Conde Nast Publications Inc.

     arstechnia.com is not available.

     Domain: arstechnia.com
     Registrar: Key-Systems GmbH
     Created: 2000-12-07 05:45:00
     Updated: [datetime.datetime(2022, 12, 8, 8, 3, 18), datetime.datetime(2023, 1, 11, 7, 14, 26)]
     Expires: 2023-12-07 05:45:00
     Whois Server: whois.rrpproxy.net
     Name Server: NS1.PARKINGCREW.NET
     Registrant: On behalf of arstechnia.com OWNER
     Orgnization: c/o whoisproxy.com

     made_up_domain.com is available.

## Notes

If using an external list of domain names, ensure there is only one name per line.

The --list flag must be followed by the location of the external file. 
domain_checker.py -l -d domain_names.txt will not work


