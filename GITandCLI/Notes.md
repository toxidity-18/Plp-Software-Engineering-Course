# Day 2 
## CLI and GIT 
- CLI help you 'chat' with your computer through it own language .
### Linux terminal commands .
___
```bash
# creating empty files
touch my_document.txt

# renaming this file
mv my_document.txt new_document.txt

# copy this file
cp new_document.txt backup_document.txt 

# move file to another location
mv backup_document.txt /path/to/destination
```
### GIT and GITHUB 
```bash
# track file inside my folder 
git init 
# adding a file or changes 
git add .
# commit my changes 
git commit -m ' commit message'
# clone a repository 
git clone ' http or the ssh link to my repo'
# creating a branch 
git branch new_feature 
# change into that branch 
git checkout new_feature 
# merge branches or to combine them 
git merge new_feature 
# to push changes 
git push origin main 
```
## Advanced github 
###  Interactive rebase
- This allows us to change commit message , reorder commit message ,delete commits , combine multiple commits into one and edit existing commit messages .
```bash 
# showing commit history 
git log --oneline 
# selecting how far back you want to go 
git rebase -i HEAD ~ 'choose how far back you want to go'
# choosing what action you want to do 
# reword (change the name of the commit message), squash (combine two commit messages) 
# ctrl+o , enter , ctrl+x
# edit the commit message or the commit itself 
# ctrl+o, enter, ctrl+x
# confirmation ..
git append # changes the most recent commit message .
# pull changes from remote repo 
git pull --ff-only origin main
```

### Cherry picking 
- Select and interact with specific commit .

## [ 20 | July | 2025 ]   

- Commit to the wrong branch eg to main instead of the feature branch .
```bash 
# switch to the feature branch 
 git checkout 'feature branch name'
 # cherry pick and the hash of the commit 
 git cherry-pick 'hash'
 # clean up the main branch after cherry picking your wrong commit 
 git checkout main
 git reset --hard HEAD~1
 ```

 ### Reflog(reference log)
 - Logs every movement of the head pointer .
 - squash , merge ... etc 

 - Recovering deleted commit messages 
 ```bash 
 ## you delete commit messages using 
 git reset --hard 'hash of commit'
 ## best approach create a new branch which makes your work space cleaner 
 git reflog # summary of all commit done 
 git branch 'name of branch' '' hash of commit you want restored .'
 ## recover deleted branches 
 ```
 