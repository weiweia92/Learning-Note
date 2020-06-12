## Copying files and directories

copy a file named file.txt to file named file2.txt in the current directory.If the destination file exists, it will be overwritten.   
`cp file.txt file2.txt`   
`-i:interactive`  
`-p:preserve the file mode`  
`eg: cp -i file.txt file_backup.txt`  

`uname -a :system info--all`  

`scp`  

## Group

Linux groups are organization units that are used to organize and administer user accounts in Linux. The primary purpose of groups is to define a set of privileges such as reading(r), writing(w), or executing(x) permission for a given resource that can be shared among the users within the group.  

There are two types of groups in Linux operating systems:  
Primary group - When a user creates a file, the file’s group is set to the user’s primary group. Usually, the name of the group is the same as the name of the user. The information about the user’s primary group is stored in the /etc/passwd file.  

Secondary or supplementary group - Useful when you want to grant certain file permissions to a set of users who are members of the group. For example, if you add a specific user to the docker group, the user will inherit the access rights from the group, and be able to run docker commands.  

Only root or users with sudo access can add a user to a group  

### add an existing user to group/multi_group  
`sudo username -a -G groupname username`  
`sudo username -a oG groupname1 groupname2 username`  
### remove a user from a group  
`sudo gpasswd -d username groupname`  
### create a group  
`sudo groupadd groupname`  
### delete a group  
`sudo groupdel groupname`  
### change a user's primary group  
To change a user primary group, use the usermod command followed by the -g option.In the following example, we are changing the primary group of the user linuxize to developers:  
`sudo usermod -g developers  username`  
### create a new user and assign groups in one command  
`sudo useradd -g users -G wheel,developers nathan`  
### display user groups  
`id username`  
### display the user's supplementary groups  
`groups liuwei`  





