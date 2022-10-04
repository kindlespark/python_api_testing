import requests
from dotenv import load_dotenv
import os 
import csv

# load environment global constants 
load_dotenv()
URL = os.getenv("URL")
filepath = os.getenv("OUTPUT_CSV_FILEPATH")

# id = "1225"
id = input("Enter id : \n")

# function 
def get_tool_detail(URL, id):                              # function signature
    # get single tool details using API request (using GET method)
    res=requests.get(URL + "/" + id)

    # assert res.status_code == 200, res.status_code

    print("HTTP status code is:", res.status_code)
    print("\nAPI response payload", res.text)
    
    # load json data output to csv file
    response = res.json()
    header = response.keys()
    data = response.values()
    filename = "/output.csv"
    data_file = open(filepath+filename, 'w', newline='')
    csv_writer = csv.writer(data_file)
    csv_writer.writerow(header)
    csv_writer.writerow(data)
    data_file.close()
    
    return res.status_code

# call get_tool_detail function
result = get_tool_detail(URL, id)
print("Result is: ", result)