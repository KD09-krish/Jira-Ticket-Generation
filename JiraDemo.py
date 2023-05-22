import jira as jira
import requests
import json
import pandas as pd
from requests.auth import HTTPBasicAuth

# Tasks to be accomplished:
# read the excel sheet, using those values we need to populate the issue fields.
# edit the fields using the script.
#  Title creation via scripts.

# configurations.
url = "https://krishna-dahale.atlassian.net/rest/api/3/issue"
url1 = "https://krishna-dahale.atlassian.net/rest/api/3/field/customfield_10040/context/10145/option"
auth = HTTPBasicAuth("dahalekrishna09@gmail.com","ATATT3xFfGF0sZkQvs8HL3f-wQbQTaJKRadZz9O8vkfxv0jDVGeaNV7m_jV6kCpYQ_TeAcS8UiRjacTwjHpDRaOp_WPhZessHqfBDP5DAx7m1cwT737oYF1-sciydEIn9-caW6BvMKUtcKfV4g5Yc7KSSWolrQd6JboV-0ZuDUsbLC_675ZINXw=FCEC6BF7")

# Https authentication check for deployment.
# A way to get the complete information of the issue page. (All the fields including the custom fields).
# Deploy this application.
# Abstract Document.

# defining the headers.
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}
# defining the project key
projectKey = "QAT1"

# read the csv using pandas
file = "C:\\Users\\91852\\Downloads\\CPV statement format.xlsx"
df = pd.DataFrame(pd.read_excel(file))
print(df)
statement = df["Statement"].values[0]
print('the following statement is ',statement)

print("inside payload")
payload = json.dumps({
    "fields": {
        "project": {"key": "QAT1"},
        "summary": "Title to be given here",
        "description":{
          "type": "doc",
          "version": 1,
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": f"{statement}"
                }
              ]
            }
          ]
        },
        "issuetype": {"name": "Bug"},
    }
})

# to add the options in the custom field.
payload1 = json.dumps({
  "options": [
    {
      "disabled": False,
      "value": "Mumbai"
    },
  ]
})
print('after payload')
# query = {
#     'jql' : 'Action = Yes',
# }
response = requests.post(
    url=url,
    headers=headers,
    data=payload,
    auth=auth,
    # params = query
)

# to populate the custom_issue field.
response1 = requests.post(
    url=url1,
    headers=headers,
    data=payload1,
    auth=auth,
)
# to verify wether the responses are succesfully recorded.
print(response.status_code)
print('after response',response.text)
print("this response is for the url1 ",response1.status_code)
print('after url1 response ',response1.text)






