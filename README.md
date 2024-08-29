# precinct-api-py
Python Scripts for interacting with WitFoo Precinct API

# Usage
1) Copy and update settings.example.yaml
2) Import the correct API version of `precinct-lib.py`
3) Create a PrecinctAPI object: `api = PrecinctAPI()`
4) Load the settings file: `api.load_settings('./6.4/settings.example.yaml')`
5) Login: `api.login()`
6) Perform supported operations against `api` object
See: `example.py` for usage examples.

# Current Calls
- `login()` - Login to Precinct using url, username and password in setttings file
- `get(endpoint)` - Generic GET
- `post(endpoint, data)` - Generic POST
- `put(endpoint, data)` - Generic PUT
- `create_leadrule(json)` - Post a new lead rule to Precinct
- `get_leadrules()` - Get all search results
- `create_search_job(json)` - Post a new search job to Precinct
- `get_search_job_list()` - Get list of all search jobs
- `get_search_job(id)` - Get the details of a particular job
- `delete_search_job(id)` - Delete a search job