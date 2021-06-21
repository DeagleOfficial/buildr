import os
import sys
from git  import Repo
import requests
import traceback

def create_github():
    token = os.getenv('GITHUB_TOKEN')
    if token == None:
        inp = input("Enter your GitHub access token: ")
        os.environ['GITHUB_TOKEN'] = inp
        os.system('setx GITHUB_TOKEN ' + inp)
        # print (os.getenv('GITHUB_TOKEN'))
    
    api = "https://api.github.com"
    payload = '{"name": "' + sys.argv[1] + '"}'
    headers = {
        "Authorization": "token " + os.getenv('GITHUB_TOKEN'), 
        "Accept": "application/vnd.github.v3+json"
    }

    r = requests.post(api + "/user/repos", data=payload, headers=headers)
    
    info = requests.get(api + "/user", headers=headers).json()

    global name
    name = info['login']
    # print (name)

def create_git():
    path = os.getcwd() + "\\" + sys.argv[1]
    Repo.init(path)
    os.chdir(path)
    os.system('echo # ' + sys.argv[1] + ' >> README.md')
    os.system('git add README.md')
    os.system('git commit -m "first commit"')
    os.system('git branch -M master')
    os.system('git remote add origin https://github.com/' + name + "/" + sys.argv[1] + ".git")
    os.system('git push -u origin master')


name = ""
try:
    create_github()
    create_git()
    print ("Created project succesfully")
except:
    traceback.print_exc()