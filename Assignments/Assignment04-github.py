# to use this install package
# pip install PyGithub
from github import Github
import requests
from config import config as cfg

apikey = cfg["githubkey"]
g = Github(apikey)

# https://github.com/katel85/aprivateone.git
privaterepo="katel85/aprivateone"
repo = g.get_repo(privaterepo)
print(repo.clone_url)
#print(repo)
fileInfo = repo.get_contents("test.txt")
urlOfFile= fileInfo.download_url
#print (urlOfFile)
response = requests.get(urlOfFile)
# output the contents of the file
contentOfFile = response.text
#print (contentOfFile)
#change contents
newContent= contentOfFile.replace("Andrew","Kate")
#print (newContents)
# sha(unique ID for the commit) as parameters
gitHubResponse=repo.update_file(fileInfo.path,"udated names",newContent,fileInfo.sha)
print (gitHubResponse)



                               

