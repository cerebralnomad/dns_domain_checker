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

## Notes

If using an external list of domain names, ensure there is only one name per line.

The --list flag must be followed by the location of the external file. 
domain_checker.py -l -d domain_names.txt will not work


