# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

for repo in g.get_user().get_repos():
    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
# make sure this replository exists, and that the path is correct
# https://github.com/katel85/data-representation-coursework.git
repo = g.get_repo("katel85/data-representation-coursework")
print(repo.clone_url)
print(repo)
# C:\Users\kate_\Data Representation\data-representation-coursework\Labs\Week5 API-OAuth copy path
fileInfo = repo.get_contents("test.txt")
#urlOfFile= fileInfo.download_url
#print (urlOfFile)
#response = requests.get(urlOfFile)
#contentOfFile = response.text
#print (contentOfFile)
#newContents = contentOfFile + " more stuff 2 \n"
#print (newContents)
#gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
#print (gitHubResponse)

