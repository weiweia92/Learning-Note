## Conda
### Conda->Package Manager+Environment Manager
Package Manager：当安装一个包的时候，依赖包  
Environment Manager：create multiple virtual environment  
1.更新conda：`conda update conda`  
2.更新anaconda：`conda update anaconda`  
3.更新python：`conda update python`  
#### Environment
1.查看系统环境，用户安装的不同Python环境会放在`~/miniconda3/envs`目录下  
conda info -e 或者 conda env list：查看当前系统中已经安装了哪些环境  
2.创建环境名字为ai37：`conda create --name ai37 python=3.7`    
3.切换到名字为ai37的环境下：`source activate ai37` 
4.返回到主环境：`source deactivate ai37`  
5.删除名为ai37的环境：`conda remove --name ai37 --all`  
#### Package
1.为当前环境安装库：`conda install <package_name>`   **conda 会从远程搜索<package_name>相关信息及依赖包**   
2.查看当前环境所有包：`conda list`   
3.查看某个环境已安装包：`conda list -n <env_name>`  
4.搜索package信息：`conda search <package_name>`  
5.安装package到指定的环境：`conda install -n py35 numpy # 如果不用-n指定环境名称，则被安装在当前活跃环境,也可以通过-c指定通过某个channel安装`   
6.更新package：`conda update -n <env_name> <package_name>`  
7.删除package：`conda remove -n <env_name> <package_name>`  

#### Channels
channels:the path or the location where conda looks for the packages that we want to install.  
1.查看当前channel:`conda config --show channels`  
2.安装特定channel下的包:`conda install -c pytorch pytorch`  (此pytorch channel仅使用了一次，并没有加入到channel list中) 
3.condaforge.com:A community-led collection of recipes, build infrastructure and distributions for the conda package manager  
  `conda config --add channels conda-forge`  
4.往默认channel中填加新的channel:`conda config -add channels pytorch`  
                              `conda install pytorch`  
                              `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/`   
                              `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/`  
                              `conda config --set show_channel_urls yes`  
**We deactivate the environment,not the channel**  
