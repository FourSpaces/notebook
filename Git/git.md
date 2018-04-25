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





```shell
bogon:crawler_taobao weicheng$ git pull
Already up-to-date.
bogon:crawler_taobao weicheng$ git --help
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory <将存储库克隆到新目录中>
   init       Create an empty Git repository or reinitialize an existing one
   			  创建一个空的Git存储库或重新初始化现有的存储库

<在当前的变化上工作（另请参阅：每天的git帮助）>
work on the current change (see also: git help everyday)

   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state <将当前HEAD重置为指定状态>
   rm         Remove files from the working tree and from the index <从工作树和索引中删除文件>

<检查历史和状态（另请参阅：git帮助修订版）>
examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   			  <使用二分查找找到引入错误的提交>
   grep       Print lines matching a pattern	<打印符合图案的线条>
   log        Show commit logs
   show       Show various types of objects		<显示各种类型的对象>
   status     Show the working tree status		<显示工作树的状态>

<成长，标记和调整你的共同历史>
grow, mark and tweak your common history
   branch     List, create, or delete branches <列出，创建或删除分支>
   checkout   Switch branches or restore working tree files <切换分支或恢复工作树文件>
   commit     Record changes to the repository <记录对存储库的更改>
   diff       Show changes between commits, commit and working tree, etc 
   			  <在提交，提交和工作树等之间显示更改>
   merge      Join two or more development histories together
   			  <一起加入两个或更多发展历史, 合并分枝>
   rebase     Reapply commits on top of another base tip <重新申请在另一个基本技巧之上提交>
   tag        Create, list, delete or verify a tag object signed with GPG
   			  <创建，列出，删除或验证使用GPG签名的标签对象>

<协作（另请参阅：git help工作流程）>
collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   			  <从另一个存储库下载对象和引用>
   pull       Fetch from and integrate with another repository or a local branch
   			  <从另一个存储库或本地分支中获取并与其集成>
   push       Update remote refs along with associated objects
   			  更新远程引用以及关联的对象

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```



--------

#  Reference

## 设置和配置

> git 



## 分支与合并

> **git branch** 	列出、创建与管理工作上下文



> **git checkout**  切换到新的分支上下文, 切到某分支



> **git merge**  将分支合并到你的当前分支 



> **git log**  显示一个分支中提交的更改记录



> **git tab**  给历史记录中的某个重要的一点打上标签



##  分享与更新项目

> **git remote**  列出远端别名



> **git remote add**  为你的项目添加一个新的远端仓库



> **git remote rm**  删除现存的某个别名



> **git fetch**  从远端仓库下载新分支与数据



> **git pull**  从远端仓库提取数据并尝试合并到当前分支



> **git push**  推送你的新分支与数据到某个远端仓库

