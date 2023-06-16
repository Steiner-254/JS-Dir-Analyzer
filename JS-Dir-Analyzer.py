import subprocess
import re
import os
from colorama import init, Fore

# Initialize colorama
init()

# Define the path to the text file containing JS endpoints
js_endpoints_file = 'jsfiles.txt'

# Define the directory pattern to search for
directory_pattern = r'/(?:[^/\n]+/)*[^/\n]+/$'
# The directory pattern is defined using a regular expression.
# It matches the following pattern:
# - '/' at the start of the directory
# - '(?:[^/\n]+/)*' to match one or more segments of the directory, each segment not containing '/' or newline characters
# - '[^/\n]+' to match the last segment of the directory, not containing '/' or newline characters
# - '/' at the end of the directory

# Read the JS endpoints from the text file
with open(js_endpoints_file, 'r') as file:
    js_endpoints = file.read().splitlines()

# Loop through each JS endpoint and search for directories
for endpoint in js_endpoints:
    print(f"Analyzing {endpoint} ...")
    
    # Make a cURL request to the JS endpoint and capture the response
    try:
        response = subprocess.check_output(['curl', '-s', endpoint]).decode('utf-8')
    except subprocess.CalledProcessError:
        response = ''
    
    # Search for directories in the response
    directories = re.findall(directory_pattern, response)
    
    # If directories are found, print them
    if directories:
        print(f"Found directories in {endpoint}:")
        for directory in directories:
            print(directory)
        print()

# Print the completion message in red
print(f"{Fore.RED}Directory Extraction Completed!{Fore.RESET}")
