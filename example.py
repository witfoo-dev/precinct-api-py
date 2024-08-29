from pathlib import Path

# Get the absolute path to the precinct-lib.py file
file_path = Path("./6.4/precinct-lib.py").resolve()

# Load the PrecinctAPI class from the file
with open(file_path, "r") as file:
    exec(file.read())

# Now you can use the PrecinctAPI class in your code
api = PrecinctAPI()
api.load_settings('./6.4/settings.example.yaml')
api.login()
leadrules = api.get_leadrules()
print(leadrules)