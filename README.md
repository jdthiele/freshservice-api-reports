# Freshservice API Reports

Use the included python script to pull down the agents, agent groups, requester groups and roles from the Freshservice REST API endpoint for your tenant.

This script does handle REST API response pagination combining the results into a single CSV report per endpoint.

## Setup

On a Linux system:

```sh
git clone <URL>
cd freshservice-api-reports
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

Edit the main.py script to replace the apikey and tenant placeholders with your respective values.

```sh
python3 main.py
```

The script should give you 4 .csv files for each of the endpoints it queries. You can likely add some other endpoints as needed.
