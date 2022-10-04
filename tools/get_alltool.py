import requests

URL = "https://simple-tool-rental-api.glitch.me/tools"

#function
def get_all_tool_detail(URL):
    # function signature
    # get single tool details using API request (using GET method
    res=requests.get(URL)

    # assert res.status_code == 200, res.status_code

    print("HTTP status code is:", res.status_code)
    print("\nAPI response payload", res.text)

    return res.status_code
    # call get_all_tool_detail function 

result =get_all_tool_detail(URL)
print("Results is: ", result)
