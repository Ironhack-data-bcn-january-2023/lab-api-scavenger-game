import requests
# Define the base URL for the Github API
base_url = "https://api.github.com"

# Define the endpoint to extract list of forks
forks_endpoint = f"{base_url}/repos/ironhack-datalabs/datamad1020-rev/forks"

# Make GET request to the endpoint to retrieve the list of forks
response = requests.get(forks_endpoint)

# Create a set for the unique programming languages used
languages_set = set()

# Check if the request was successful
if response.status_code == 200:
    # Create response JSON
    forks = response.json()

    # Iterate over the forks json
    for fork in forks:
        # Define the endpoint to retrieve the programming languages used in the fork
        languages_endpoint = f"{base_url}/repos/{fork['full_name']}/languages"

        # Send a GET request to the endpoint to retrieve the programming languages used
        languages_response = requests.get(languages_endpoint)

        # Check if the request was successful
        if languages_response.status_code == 200:
            # Create another response JSON
            fork_languages = languages_response.json()

            # Add the programming languages used in the fork to the set
            languages_set.update(fork_languages.keys())

# Print the number of unique programming languages used among all the forks
print(languages_set)
