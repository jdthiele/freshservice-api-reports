import csv
import requests
from urllib3.exceptions import InsecureRequestWarning

datatypes = ["roles", "agents", "groups", "requester_groups", "requesters"]
apikey = 'APIKEYHERE'
tenant = 'YOURFRESHSERVICETENANTNAMEHERE'

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_freshservice_api(datatype):
    basic = requests.auth.HTTPBasicAuth(apikey, 'x')
    url = f"https://{tenant}.freshservice.com/api/v2/{datatype}"
    s = requests.Session()
    print(url)
    response = s.get(url, auth=basic, verify=False)
    results = []
    resp_json = response.json()
    print(len(resp_json[datatype]))
    results = (resp_json[datatype])
    while response.links.get('next', None) is not None:
        url=response.links['next']['url']
        print(url)
        response = s.get(url, auth=basic, verify=False)
        resp_json = response.json()
        print(len(resp_json[datatype]))
        [results.append(item) for item in resp_json[datatype]]
    return results

for datatype in datatypes:
    print(f'\nStarting datatype: {datatype}\n')
    results = get_freshservice_api(datatype)

    print(len(results))

    with open(f"{datatype}.csv", 'w', newline='') as f_out:
        fieldnames = list(results[0].keys())
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(results)
