## A class for connecting to the Precinct API
import requests
import json
import yaml
import urllib3

# Disable InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class PrecinctAPI:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def load_settings(self, settings_file='settings.yaml'):
        with open(settings_file, 'r') as file:
            settings = yaml.safe_load(file)
            self.base_url = settings['base_url']
            self.username = settings['username']
            self.password = settings['password']
        return settings

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, headers=self.headers, data=json.dumps(data), verify=False)
        try:
            return response.json()
        except json.JSONDecodeError:
            print(f"Failed to decode JSON response: {response.text}")
            response.raise_for_status()

    def put(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=self.headers, data=json.dumps(data), verify=False)
        try:
            return response.json()
        except json.JSONDecodeError:
            print(f"Failed to decode JSON response: {response.text}")
            response.raise_for_status()

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=self.headers, verify=False)
        try:
            return response.json()
        except json.JSONDecodeError:
            print(f"Failed to decode JSON response: {response.text}")
            response.raise_for_status()

    def login(self):
        data = {'email': self.username, 'password': self.password}
        response = self.post('v1/login', data)
        self.token = response['token']
        self.headers['API-Token'] = f"{self.token}"
        return response

    def get_leadrules(self):
        return self.get('v1/api/lead_rules')
    
    def create_leadrule(self, data):
        return self.post('v1/api/lead_rules', data)
    
    def get_search_job_list(self):
        return self.get('v1/api/search/jobs/list')
    
    def get_search_job(self, job_id):
        return self.get(f'v1/api/search/jobs/get/{job_id}')
    
    def create_search_job(self, data):
        return self.post(f'v1/api/search/jobs/create/{data}')
    
    def delete_search_job(self, job_id):
        return self.put(f'v1/api/search/jobs/{job_id}')