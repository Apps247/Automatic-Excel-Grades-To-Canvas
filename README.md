# Excel Grades to Canvas (Designed for UBC CPSC 121)

*Note: This script relies on specific formatting consistent with CPSC 121 Lab Grades Formatting as of October 2023.*

## Requirements
* Python 3.5 or higher
* Packages included in `requirements.txt`, can be installed with `pip3 install -r requirements.txt`
* User has write access to Canvas course (set by default to CPSC 121 2023W1). API Key can be generated in Canvas > Profile > New Access Token. Paste the access token in `sample.env`, ensuring the file reads 
`
CANVAS_API_TOKEN=YOUR_TOKEN_HERE
`

## Usage
Run `python3 main.py`
Ensure the Lab Grades spreadsheet in the `lab_excel_sheets` folder 

Input the Lab sections (eg: enter "L1C L13 L11" without the quotes, separated by spaces) and Lab number (enter 4 for Lab 04). Confirm that the displayed details loaded from the Canvas API are correct.

Note: for testing purposes, `lab_no_spoof` in `main.py` can be adjusted to update another column in the gradebook, if the actual lab has already been filled up.

Logs are available in `log.txt`

## TODO
* Input excel file using path, rather than requiring presense in directory
* OneDrive integration
* More polished UI 