import os
import csv 
from datetime import datetime

# CSV FILE
csv_file = os.path.join('employee_data.csv')


# DICTIONARY OF STATES WITH ABBREVIATIONS
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# MAKE LISTS TO STORE THE DATA
empl_id = []
empl_first_name = []
empl_last_name = []
empl_dob = []
empl_ssn = []
empl_state = []
Header = ["Emp ID", "First Name", "Last Name", "DOB",
               "SSN", "State"]


# OPEN AND READ THE CSV FILE
with open (csv_file,newline="") as csvfile :
    csv_reader = csv.reader(csvfile, delimiter=",")

    # SKIP THE HEADER
    csv_header = next(csv_reader)

    for row in csv_reader:

        # STORE empl_id INTO A LIST
        empl_id.append(row[0])

        # SPLIT THE FULL NAME AND STORE IT
        split_name = row[1].split(" ")

        # SPLIT THE NAMES AND STORE IT
        empl_first_name = empl_first_name + [split_name[0]]
        empl_last_name = empl_last_name + [split_name[1]]

     
        # MODIFY THE DATE OF BIRTH FORMAT 
        date_split = datetime.strptime(row[2], "%Y-%d-%m").strftime("%m/%d/%Y")
        
        # STORE THE DOB INTO A LIST
        empl_dob = empl_dob + [date_split]
        

        # MODIFY SSN
        reform_ssn = "***-**-" + row[3].split(7)
        empl_ssn = empl_ssn + [reform_ssn]

        

        # CHANGE THE STATES NAME TO THIER ABBREVIATIONS
        state_abbrev = us_state_abbrev[row[4]]
        empl_state = empl_state + [state_abbrev]

        


# COLLECT ALL THE LISTS TOGETHER (ZIP)
employee_data = zip(empl_id,empl_first_name,empl_last_name,empl_dob,
empl_ssn,empl_state)


text_export = os.path.join("Modified_Data.txt")

with open(text_export,"w",newline="") as text_file:
    csv_writer = csv.writer(text_file)
    
    csv_writer.writerow(empl_first_name)
    csv_writer.writerow(empl_last_name)
    csv_writer.writerow(empl_dob)
    csv_writer.writerow(empl_ssn)
    csv_writer.writerow(empl_state)
    