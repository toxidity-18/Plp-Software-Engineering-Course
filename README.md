# Plp-Software-Engineering-Essentials
Power Learn Project  Academy .

# Lesson Objectives 
1) Understand what software engineering is and how it is important in todays world .
2) Key skill of a software engineer .
3) Appreciate how soft engineers solve real world problems .
# Day 1
## What is software engineering about :
- It about writing instructions or line of code , building games , apps , websites and solving real world problems .
 
 ### Their work 
  1.  Design system and apps . 
  2. Write code , test it , fix bugs 
  3. Collaborate with a team to create amazing stuffs .

### Magic tools of software engineers 
  1. Programming languages 
  2. Code editor eg vsc where all the magic take effect .
  3. Version control systems .

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
git rebase -i HEAD ~ 'choose how far back you want to go'
# apply reword on the selected commit message 
# ctrl+o , enter , ctrl+x
# edit the commit message 
# ctrl+o, enter, ctrl+x
# check if you successfully change the commit message name .
git append # changes the most recent commit message .
