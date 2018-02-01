# texts_and_calls_analysis
## Overview
In this Project, there are five tasks based on a fabricated set of calls and texts exchanged during September 2016. 
Use Python to analyze and answer questions about the texts and calls contained in the dataset.

### About data
The text and call data are provided in csv files. In each file, the data is already read and stored as lists of lists.

Each sub-list of the list of texts is structured in this way:
```
a text = [	Sending telephone number (string),
		receiving telephone number (string), 
		timestamp of text message (string)]
```
Each element in the list of phone calls is structured in this way:
```
a call = [	Calling telephone number (string), 
		receiving telephone number (string), 
		start timestamp of telephone call (string),
		duration of telephone call in seconds (string)]
```
All telephone numbers are 10 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:

- Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: (022)40840621.
- Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: 93412 66159.
- Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: 1402316533.

### About the goals
 Tasks         | Specifications    
 ------------- | -----------------
Task 0   | successful	The script correctly prints out the infomation of first record of texts and last record of calls
Task 1   | successful	The script correctly prints number of distinct telephone numbers in the dataset.
Task 2   | successful	The script correctly prints the telephone number that spent the longest time on the phone and the the total time in seconds they spend on phone call.
Task 3   | successful	The script correctly prints the telephone codes called by fixed-line numbers in Bangalore and the proportion of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.
Task 4   | successful	The script correctly prints the list of numbers that could be telemarketers.
