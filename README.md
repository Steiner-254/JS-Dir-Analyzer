# JS-Dir-Analyzer
JS-Dir-Analyzer

# JS Directory Extraction Tool

The JS Directory Extraction Tool is a Python script that helps you extract directories from JS files. It searches for directory patterns within the responses of provided JS endpoints and outputs the discovered directories.

## Requirements

- Python 3.x
- `curl` command-line tool

## Installation

1. Clone this repository or download the `script.py` file.
2. Ensure that Python 3 is installed on your system.
3. Install the required Python packages by running the following command:

pip install colorama

## Usage

1. Prepare a text file `jsfiles.txt` that contains the URLs of the JS files you want to analyze. Each URL should be on a separate line.
2. Run the script using the following command:

python3 script.py

The script will analyze the JS files, search for directories, and print any directories found.
3. The script will display the completion message "Directory Extraction Completed!" in red.

## Customization

- Modify the `jsfiles.txt` file to include the URLs of the JS files you want to analyze.
- Adjust the regular expression pattern (`directory_pattern`) in the script if you want to match different directory formats.


