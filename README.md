# subtrail
## Description
This script is designed to pull down all subdomains from Security Trails for a given domain

You must specify your api key from: https://securitytrails.com/

### Example Usage

``subtrail.py -d example.com -r -o example_subdomains.txt``

By default if no output file is specified the results will be saved in subdomains.lst. Add the ``-r`` flag to resolve the subdomains to IP addresses if available.
