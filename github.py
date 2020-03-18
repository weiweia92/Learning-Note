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