# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

#for repo in g.get_user().get_repos():
    #print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))
# make sure this replository exists, and that the path is correct
# https://github.com/katel85/aprivateone.git
privaterepo="katel85/aprivateone"
repo = g.get_repo(privaterepo)
print(repo.clone_url)
#print(repo)
fileInfo = repo.get_contents("test.txt")
urlOfFile= fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)
#change contents
newContent= contentOfFile.replace("Andrew","Kate")
#print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"udated names",newContent,fileInfo.sha)
print (gitHubResponse)



                               

