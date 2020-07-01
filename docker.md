## Docker  

## Docker教程  
### docker安装  
`sudo apt-get install docker.io`  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-42-41.png)  
安装成功  
`docker info`:查看docker信息  
此时的docker是一个‘裸’docker，没有container也没有image，image简单理解就是container的只读版，用来方便存储与交流  
我们可以通过官方提供给我们的镜像来进行学习。比如我们想在Docker中运行一个Ubuntu系统，很简单，Docker中得pull命令是用来获取镜像的，执行下面的命令，就会从官方仓库里获取Ubuntu 18.04版本的系统:  
`docker pull ubuntu:18.04`  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-43-02.png)
`-it`:表示交互  
仔细看，你会发现终端交互的用户名变掉了，说明我们进入到了容器的内部,执行`exit`退出此终端，回到系统本身的终端  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-43-23.png)
`docker ps`:查看当前运行了哪些容器  
`docker ps -a`:表示运行过哪些容器  
`sudo docker commit -m "Added ubuntu18.04" -a "weiweia92" 79c761f627f3 weiweia92/ubuntu:v1`  
`commit`命令用来将容器转化为镜像  
 `m`用来来指定提交的说明信息；`-a`可以指定用户信息的；`79c761f627f3`代表容器的id；weiweia92/ubuntu:v1指定目标镜像的用户名、仓库名和 tag 信息  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-44-00.png)

`docker images`:查看拥有的镜像  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-44-12.png)
里面有一个test镜像tag为0.1  
`docker run -it test:0.1`:进入名为test的镜像  

### 如何将建立好的镜像上传到dockerhub上  
首先打开dockerhub登录自己的账号,建立一个新的仓库，仓库的名字要和待上传的镜像名字一致,实例中叫test  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-44-23.png)
在终端执行`docker push weiweia92/test:0.1`  
![](https://github.com/weiweia92/pictures/blob/master/Screenshot%20from%202020-07-01%2009-44-32.png)
将yolov4模型的test镜像上传到dockerhub上  
在所要运行的服务器上执行`docker pull weiweia92/test:0.1`即将镜像拉到服务器上  
执行`docker run -it test:0.1`进入到镜像内  
完毕！
  




最好建立一个文件夹专门放Dockerfile的  
`mkdir docker-sample && cd docker-sample`  
`touch Dockerfile`
  
### Dockerfile语法  

**FROM**   
Dockerfile第一条必须为FROM指令，选择parent image for docker,为了安全尽量使用官方的base image，如果同一个Dockerfile创建多个镜像时，可使用多个FROM指令：  
`FORM scratch`&emsp;&emsp;&emsp;#制作base image    
`FORM centos`&emsp;&emsp;&emsp;#使用base image    
`FORM centos`：14.04 &emsp;&emsp;&emsp;#使用带版本的base image  
  
**LABEL**  
LABEL用于定义Metadata，包括作者信息，版本信息，描述信息  
`LABEL maintainer="starlihang@qq.com"`     
`LABEL version="1.0"`  
`LABEL description="hello docker"`  

**RUN**   

**WORKDIR**  
设定当前的工作目录,尽量使用WORKDIR切换工作目录，避免使用RUN cd！尽量使用绝对目录  
`WORKDIR /test`&emsp;&emsp;&emsp;#切换到test目录，如果没有会自动创建test目录  
`WORKDIR hello`    

**RUN**  
RUN instruction runs commands,just like you do on the terminal,but in the Docker image.  
下面的命令用来安装Python, pip和app dependencies,dependencies写在rerequirements.txt文件里.  

`RUN apk add --update python py-pip`  
`RUN pip install --upgrade pip`  
`RUN pip install -r requirements.txt`    

**ADD and COPY**  
添加/复制文件到指定目录。优先使用COPY，ADD还有解压，添加远程文件或目录使用curl或者wget的作用    
`ADD hello /`&emsp;&emsp;&emsp;# 添加hello到根目录  
`ADD test.tar.gz /`&emsp;&emsp;&emsp;# 添加到根目录并解压(COPY不会解压）  
`WORKDIR /root` &emsp;&emsp;&emsp;# 切换到root目录  
`ADD hello test/` &emsp;&emsp;&emsp;# /root/test/hello  
为什么要使用COPY而不是ADD？你会发现从URL复制文件是一项可以使用RUN命令通过Curl运行的任务。您也可以使用RUN命令在Docker映像中提取文件。  
`COPY hello test`    

**WORKDIR**  
WORKDIR允许你在Docker建立image时更改目录，the new directory remains the current directory for the rest of the build instructions.

**MAINTAINER**  
MAINTAINER <name>  
指令允许您设置生成的images的作者字段  

**ENV**  
设置常量，多使用常量增加可维护性  
`ENV applocation /usr/src `  
`COPY flask-helloworld $applocation/flask-helloworld`  
`ENV flaskapp $applocation/flask-helloworld`  
WORKDIR instruction changes the current directory in Docker image.The command below changes directory to /usr/src/flask-helloworld.The target directory uses the environment variable.  
`WORKDIR $flaskapp/`  

**CMD and ENTRYPOINT**  
CMD  
CMD instruction runs commands like RUN,but the commands run when the Docker container launches.Only one CMD instruction can be used.  
`CMD ["python", "app.py"]`  

ENTRYPOINT：  
    * 设置容器启动时运行的命令  
    * 让容器以应用程序或者服务的形式运行（后台进程）  
    * 不会被忽略，一定会执行  
    * 常见使用方式：写一个脚本作为ENTRYPOINT去执行  
PS：RUN是执行命令并创建新的image layer  

**VOLUME and EXPOSE**  
存储和网络设置，VOLUME创建一个可以从本地主机或其他容器挂载的挂载点，一般用来存放数据库和需要保持的数据。EXPOSE 告诉Docker服务端容器暴露的端口号，供互联系统使用。在启动Docker时，可以通过-P,主机会自动分配一个端口号转发到指定的端口，如：

`docker run -d -p 127.0.0.1:23333:22 centos6-ssh`:容器ssh服务的22端口将被映射到宿主机的23333端口  

### 根据Dockerfile创建docker image  
建立完一个sample_image/Dockerfile后，创建docker image  
`sudo docker build -t sample_image .`  

### 运行Docker container   
`sudo docker run -ip 5000:5000 sample_image:latest`  
-i:交互  
-p:docker host port:Docker container port  

