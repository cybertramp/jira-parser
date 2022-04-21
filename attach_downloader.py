#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This tool created to easily receive jira attachments.

2022.04.21
paran_son@outlook.com
"""

import requests
from requests.auth import HTTPBasicAuth
import json
import os
import configparser

# frame file info
file_info = {
    "issue_name": "",
    "id": 0,
    "created": "",
    "filename": "",
    "size": "",
    "content": ""
}

# return auth info
def read_setup_config(path: str):
    '''
    read setup config file
    '''
    config = configparser.ConfigParser()    
    config.read(path, encoding='utf-8')

    email = config.get('auth', 'email')
    token = config.get('auth', 'token')
    url = config.get('info', 'jira_url')

    print(email, token, url)

    return email, token, url

# return issue
def read_issue_lst(path: str):
    '''
    read issue list
    '''
    with open(path, "r") as txt_file:
        issues = txt_file.read().splitlines()

    print("Issues")
    for i in issues:
        print(i)

    return issues

def worker():

    lst_attach = []
    res = []

    auth_email, auth_token, info_url = read_setup_config("setup.conf")
    auth = HTTPBasicAuth(auth_email, auth_token)

    info_url = "https://" + info_url + "/rest/api/3/issue"

    lst_issue = read_issue_lst("issues.txt")

    headers_json = {"Accept": "application/json"}

    output_dir = "output/"

    # check exist output directory
    if os.path.isdir(output_dir) is False:
        os.mkdir(output_dir)
    
    # repeat issue items
    for id_issue in lst_issue:
        url = info_url+ "/" +id_issue
        response = requests.request(
            "GET",
            url,
            headers=headers_json,
            auth=auth
        )

        res_json = json.loads(response.text)
        res_json = res_json["fields"]["attachment"]

        # repeat attachment count
        for idx_attach, data_attach in enumerate(res_json):
            file_info = {
                "issue_name": id_issue,
                "id": data_attach["id"],
                "created": data_attach["created"],
                "filename": data_attach["filename"].replace(' ', ''),
                "size": data_attach["size"],
                "content": data_attach["content"]
            }
            lst_attach.append(file_info)

            if os.path.isfile(output_dir+file_info["filename"]):
                print("File already Exist:", output_dir+file_info["filename"])
                continue

            with open(output_dir+file_info["filename"], "wb") as file:
                #headers_zip = {'Content-Type': 'application/zip; charset=utf-8', 'Accept-Ranges': 'bytes', 'Content-Length': str(data_attach["size"])}
                response = requests.get(file_info["content"], auth=auth, timeout=5)
                file.write(response.content)
                print("Downloaded "+file_info["filename"]+" ("+file_info["content"]+")")
                
        res += lst_attach
    
    # save result with json
    # this file will be use before exist check with filename
    with open("data.json", "w") as json_file:
        json.dump(res, json_file)

def main():
    worker()

if __name__ == "__main__":
    main()
