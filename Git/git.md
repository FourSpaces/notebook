#### 创建仓库，提交代码到仓库的过程

echo "# tianqibao" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:zaoshu/tianqibao.git

git push origin master

####  

#### cd  到指定目录下，添加本地仓库

git init
#### 添加文件 到本地仓库

git add README.md
#### 提交文件记录

git commit -m "first commit"

#### 添加远程仓库

git remote add origin git@github.com:zaoshu/tianqibao.git

git remote add scrapy_zs git@github.com:zaoshu/scrapy_zs.git

#### push 到远程

git push origin master



#### clone 指定分支下的

使用Git下载指定分支命令为：**git clone -b ****分支名****仓库地址**
```
#使用Git下载v.2.8.1分支代码，使用命令：
git clone -b v2.8.1 https://git.oschina.net/oschina/android-app.git

```

　　