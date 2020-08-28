import sys
import requests
import argparse

api_key = ""

if api_key == '':
    sys.exit('\nPlease edit the script to include an API KEY\n')

description = "This script is designed to pull down all subdomains for a given domain"

epilog = """
EXAMPLE USAGE:
An API KEY must be specified within the script!

subtrail.py -d example.com -o example_subdomains.txt
By default if no output file is specified the results will be saved in subdomains.lst
"""

parser = argparse.ArgumentParser(
    description=description, epilog=epilog, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-d", "--domain", required=True,
                    help="The domain excluding the @ sign (example.com)")
parser.add_argument("-o", "--outfile", default="subdomains.lst",
                    help="Outputs enumerated users to file you specify.")
args = parser.parse_args()

url = 'https://api.securitytrails.com/v1/domain/' + args.domain + '/subdomains'

try:
    domain = sys.argv[1]
except NameError:
    print("please provide a domian name: " + sys.argv[0] + ' domain.com')
apiKey = {'apikey': api_key}
x = requests.get(url, headers=apiKey)
jsonResp = x.json()

with open(args.outfile, 'w') as file:
    for sub in jsonResp['subdomains']:
        fqdn = sub + '.' + args.domain
        print(fqdn)
        file.write(fqdn + '\n')

print('\nResults were written to ' + args.outfile)
