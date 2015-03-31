import json

with open(".fb_access_token") as json_file:
    json_data = json.load(json_file)
    print(json_data['access_token'])
