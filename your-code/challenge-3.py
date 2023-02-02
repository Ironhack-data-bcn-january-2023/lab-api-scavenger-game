import requests
import re

# Define the API endpoint
api_endpoint = "https://api.github.com/repos/ironhack-datalabs/scavenger/contents"

# Make a GET request to the API endpoint
response = requests.get(api_endpoint)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    contents = response.json()
    
    # Find the secret files
    secret_files = [content for content in contents if re.match(r'\.\d{4}\.scavengerhunt', content['name'])]
    
    if secret_files:
        # Sort the secret files by their filenames
        secret_files.sort(key=lambda x: x['name'])
        
        # Read the contents of each secret file
        contents = []
        names = []
        for secret_file in secret_files:
            names.append(secret_file['name'])
            content = secret_file['content']
            contents.append(content)
        
        # Concatenate the strings
        joke = ' '.join(contents)
        
        print(contents)

        # Print the joke
        print(joke)
    else:
        # Print an error message
        print("An error occurred:", response.status_code)
