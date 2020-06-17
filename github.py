# Github and GitLab

git --version

git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"
git config --global --list

# Create a new local repository
git init

# List the files you've changed and those you still need to add or commit
git status

# add a file to the staging area
git add <filename>
#add one or more to the staging area
git add *

#commits any files you’ve added with the git add command and also commits any files you’ve changed since then.
git commit -a

# Create a new repository on github and upload local files to it
cd <a local path>
git clone <repository SSH>
eg:git clone git@github.com:weiweia92/Learning-Note.git
cd <repository_name>
eg:ls
   cd Learning-Note
   git add <file_name>
   git commit -m '<annotation>'
   git push

# delete files/directory on github 
git rm -r <file_name/directory_name>
git commit -m '<annotation>'
git push

# add the local files/directory to github
git add <file_name/directory_name>
git commit -m '<annotation>'
git push -f

#Create a new branch and switch to it
git checkout -b <branchname>
#Switch from one branch to another
git checkout <branchname>

#Push the branch to your remote repository, so others can use it
git push origin <branchname>

# check all branch
git branch -a
# delete the local branch
git branch -d <branchname>

# delete the remote branch
git push origin --delete <branchname>

#Fetch and merge changes on the remote server to your working directory
git pull

#To merge a different branch into your active branch
git merge <branchname>

#show the file differences which are not yet staged
git diff
#shows the differences between the files in the staging area and the latest version present
git diff -staged
#View the conflicts against the base file
git diff --base <filename>
#shows the differences between the two branches mentioned.
#Preview changes, before merging
git diff <sourcebranch> <targetbranch>

#Search the working directory for foo()
git grep "foo()"

#Unstage all changes that have been added to the staging area
#To undo the most recently added, but not committed, changes to files/folders
git reset .
#Undo most recent commit,undo the most recent commit
git reset HEAD~1
#unstages the file, but it preserves the file contents.
git reset <filename>
#undoes all the commits after the specified commit and preserves the changes locally.
git reset <09bb8e3f996eaf9a68ac...>
#discards all history and goes back to the specified commit
git reset -hard <09bb8e3f996eaf9a68ac...>

#list the version history for the current branch
git log

#lists version history for a file, including the renaming of files also
git log -follow <filename>

#shows the metadata and content changes of the specified commit.
git show <09bb8e3f996eaf9a68ac...>

#Used to give tags to the specified commit
git tag <09bb8e3f996eaf9a68ac...>

#Problem
Git Error - key does not contain a section
解决:
emacs /.git/config
make core look like:
[core]
repositoryformatversion = 0
filemode = true
bare = false
logallrefupdates = true
ignorecase = true
precomposeunicode = true
