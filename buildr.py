import os
import sys
from git  import Repo
import requests
import traceback
import argparse

def create_github():
    token = os.getenv('GITHUB_TOKEN')
    if token == None:
        inp = input("Enter your GitHub access token: ")
        os.environ['GITHUB_TOKEN'] = inp
        os.system('setx GITHUB_TOKEN ' + inp)
        # print (os.getenv('GITHUB_TOKEN'))
    
    api = "https://api.github.com"
    payload = '{"name": "' + name + '"}'
    headers = {
        "Authorization": "token " + os.getenv('GITHUB_TOKEN'), 
        "Accept": "application/vnd.github.v3+json"
    }

    r = requests.post(api + "/user/repos", data=payload, headers=headers)
    
    info = requests.get(api + "/user", headers=headers).json()

    global username
    username = info['login']
    # print (username)

def create_git():
    path = os.getcwd() + "\\" + name
    Repo.init(path)
    os.chdir(path)
    os.system('echo # ' + name + ' >> README.md')
    os.system('git add README.md')
    os.system('git commit -m "Initial commit"')
    os.system('git branch -M master')
    os.system('git remote add origin https://github.com/' + username + "/" + name + ".git")
    os.system('git push -u origin master')

my_parser = argparse.ArgumentParser()
my_parser.add_argument("--name", "-n", dest="name", required=True)
name = my_parser.parse_args().name

username = ""
try:
    create_github()
    create_git()
    print ("Created project succesfully")
except:
    traceback.print_exc()