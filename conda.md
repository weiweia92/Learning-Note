## Conda
### Conda->Package Manager+Environment Manager
Package Manager：当安装一个包的时候，依赖包  
Environment Manager：create multiple virtual environment  
#### Environment
1.查看系统环境，用户安装的不同Python环境会放在`~/miniconda3/envs`目录下  
conda info -e 或者 conda env list：查看当前系统中已经安装了哪些环境  
2.创建环境名字为ai37：`conda create --name ai37 python=3.7`    
3.切换到名字为ai37的环境下：`source activate ai37`    
#### Package
1.安装包：`conda install <package_name>`    
2.查看当前环境所有包：`conda list`    
#### Channels
channels:the path or the location where conda looks for the packages that we want to install.  
