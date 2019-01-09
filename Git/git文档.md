# git 文档

## 1. 安装git

#### 在 Linux 上安装 Git

你可以试着输入 git，看看系统有没有安装 Git：

```
$ git
The program 'git' is currently not installed. You can install it by typing:
sudo apt-get install git
```

没有更新的话，已友好的告诉你如何安装git

```
$ sudo apt-get install git
```

#### 在 Mac OS X 上安装 Git

```
$ brew install git
```

####  在 Windows 上安装 Git

msysgit 是 Windows 版的 Git，从 <http://msysgit.github.io/> 下载，然后按默认选项安装即可。

安装完成后，在开始菜单里找到“Git”->“Git Bash”，蹦出一个类似命令行窗口的东西，就说明 Git 安装成功！

![img](http://wiki.jikexueyuan.com/project/git-tutorial/images/git4.jpg)

**安装完成后，还需要最后一步设置**

在命令行输入：

```
$ git config --global user.name "你的用户名"
$ git config --global user.email "你的github注册邮箱"
```

注意`git config`命令的`--global`参数，用了这个参数，表示你这台机器上所有的 Git 仓库都会使用这个配置，当然也可以对某个仓库指定不同的用户名和 Email 地址。

## 2. 创建版本库

什么是版本库呢？版本库又名仓库，英文名 repository，你可以简单理解成一个目录，这个目录里面的所有文件都可以被 Git 管理起来，每个文件的修改、删除，Git 都能跟踪，以便任何时刻都可以追踪历史，或者在将来某个时刻可以“还原”。

所以，创建一个版本库非常简单，首先，选择一个合适的地方，创建一个空目录：

```
$ mkdir learngit
$ cd learngit
$ pwd
/Users/michael/learngit
```

`pwd`命令用于显示当前目录。在我的 Mac 上，这个仓库位于`/Users/michael/learngit`。

如果你使用 Windows 系统，为了避免遇到各种莫名其妙的问题，请确保目录名（包括父目录）不包含中文。

第二步，通过`git init`命令把这个目录变成 Git 可以管理的仓库：

```
$ git init
Initialized empty Git repository in /Users/michael/learngit/.git/
```

瞬间 Git 就把仓库建好了，而且告诉你是一个空的仓库（empty Git repository）

用`ls -ah`命令就可以看见当前目录下多了一个`.git`的目录，这个目录是 Git 来跟踪管理版本库的，没事千万不要手动修改这个目录里面的文件，不然改乱了，就把 Git 仓库给破坏了。

一定要放到 learngit 目录下或子目录下

```
$ git status # 随时用git status 查看文件状态
```

一个文件放到 Git 仓库只需要两步。

1. 用命令`git add`告诉 Git，把文件添加到仓库：

```
$ git add .  # 把所有文件都添加到仓库 也可以单独添加某个文件，按照git status提示,比如
$ git add abc/aaa.py
```

执行上面的命令，没有任何显示，这就对了，Unix 的哲学是“没有消息就是好消息”，说明添加成功。

2. 用命令`git commit`告诉 Git，把文件提交到仓库：

```
$ git commit abc/aaa.py -m"chore:wrote a readme file"
[master (root-commit) cb926e7] wrote a readme file
 1 file changed, 2 insertions(+)
 create mode 100644 aaa.py
```

commit 必须遵循commit规范

**git commit规范**

- feat：新功能（feature）
- fix：修补bug
- docs：文档（documentation）
- style： 格式（不影响代码运行的变动）
- refactor：重构（即不是新增功能，也不是修改bug的代码变动）
- test：增加测试
- chore：构建过程或辅助工具的变动

## 3. 新机器配置git

1. 创建 SSH Key。在用户主目录下，看看有没有`.ssh`目录，如果有，再看看这个目录下有没有`id_rsa`和`id_rsa.pub`这两个文件，如果已经有了，可直接跳到第2步。如果没有，打开 Shell（Windows 下打开 Git Bash），创建 SSH Key：

```
$ ssh-keygen -t rsa -C "你的github邮箱"
```

把邮件地址换成你自己的邮件地址，一路回车，使用默认值即可，无需设置密码。

如果一切顺利的话，可以在用户主目录里找到`.ssh`目录，里面有 id_rsa 和 id_rsa.pub 两个文件，这两个就是 SSH Key 的秘钥对，`id_rsa`是私钥，不能泄露出去，`id_rsa.pub`是公钥，可以放心地告诉任何人。

2. 登陆 GitHub，打开“Account settings”，“SSH Keys”页面：

然后，点“Add SSH Key”，填上任意 Title，在 Key 文本框里粘贴`id_rsa.pub`文件的内容：

![img](http://wiki.jikexueyuan.com/project/git-tutorial/images/git13.png)

点“Add Key”，你就应该看到已经添加的 Key

![img](http://wiki.jikexueyuan.com/project/git-tutorial/images/git16.png)



当然，GitHub 允许你添加多个 Key。假定你有若干电脑，你一会儿在公司提交，一会儿在家里提交，只要把每台电脑的 Key 都添加到 GitHub，就可以在每台电脑上往 GitHub 推送了。

## 4. 关联远程库

1. 如果公司已创建该项目的远程库，本地还没有，clone 该项目地址: clone with ssh

    ![](/Users/offer/Desktop/clone.jpg)

   ```
   $ git clone git@github.com:xxxx/xxx.git
   ```

   #### SSH 警告

   当你第一次使用 Git 的 clone 或者 push 命令连接 GitHub 时，会得到一个警告：

   ```
   The authenticity of host 'github.com (xx.xx.xx.xx)' can't be established.
   RSA key fingerprint is xx.xx.xx.xx.xx.
   Are you sure you want to continue connecting (yes/no)?
   ```

   这是因为 Git 使用 SSH 连接，而 SSH 连接在第一次验证 GitHub 服务器的 Key 时，需要你确认 GitHub 的 Key 的指纹信息是否真的来自 GitHub 的服务器，输入 yes 回车即可。

   Git 会输出一个警告，告诉你已经把 GitHub 的 Key 添加到本机的一个信任列表里了：

   ```
   Warning: Permanently added 'github.com' (RSA) to the list of known hosts.
   ```

   这个警告只会出现一次，后面的操作就不会有任何警告了。

   ​

2. 如果已经在本地创建了一个 Git 仓库后，公司也已在 GitHub 创建一个 Git 仓库，

   - 实现让这两个仓库进行远程同步

   ```
   $ git remote add origin git@github.com:xxxx/xxxx.git
   ```

   - 下一步，就可以把本地库的所有内容推送到远程库上

     ```
     $ git push -u origin master
     ```

     把本地库的内容推送到远程，用`git push`命令，实际上是把当前分支 master 推送到远程。

     由于远程库是空的，我们第一次推送 master 分支时，加上了`-u`参数，Git 不但会把本地的 master 分支内容推送的远程新的 master 分支，还会把本地的 master 分支和远程的 master 分支关联起来，在以后的推送或者拉取时就可以简化命令。

     推送成功后，可以立刻在 GitHub 页面中看到远程库的内容已经和本地一模一样

     从现在起，只要本地作了提交，就可以通过命令：

     $ git push origin master 把本地master分支的最新修改推送至GitHub

3. 一般我们在develop分支开发

   1. 如果github上**没有develop分支**

   - 首先，我们在本地创建 develop 分支，然后切换到 develop 分支：

     ```
     $ git checkout -b develop
     Switched to a new branch 'develop'
     ```

     `git checkout`命令加上`-b`参数表示创建并切换，相当于以下两条命令：

     ```
     $ git branch develop
     $ git checkout develop
     Switched to branch 'develop'
     ```

     然后，用`git branch`命令查看当前分支：

     ```
     $ git branch
     * develop
       master
     ```

     `git branch`命令会列出所有分支，当前分支前面会标一个`*`号

   - 发布develop分支

     发布dev分支指的是同步develop分支的代码到远程服务器

     ```
     git push origin develop:develop    # 这样远程仓库也有一个develop分支了 或者
     git push origin develop  # 这两种应该都可以
     ```

   2. 如果github已经**有master分支和develop分支**

      在本地

      `git checkout -b develop ` 新建并切换到本地develop分支

      `git pull origin develop`  本地develop分支与远程develop分支相关联



## 总结

```
git add .  # 添加所有改动的文件到仓库
git commit 文件路径 -m'fix:修复xx bug'

# github上已经有master分支 和dev分支在本地
git checkout -b dev # 创建+切换分支dev
git pull origin dev # 本地分支与远程分支相关联dev

# github无dev分支，在本地新建分支并推送到远程
git checkout -b dev
git push origin dev:dev  # 这样远程仓库中也就创建了一个dev分支

git branch  # 查看本地有多少分支
git branch 分支名字 # 创建分支
git checkout dev # 切换到dev分支进行开发
git push # 提交到远程
git branch -d dev # 删除本地dev分支
git merge dev # 合并dev到当前分支(master)

```

**一般我们没有merge权限，需要提PR(pull request),加上review的人,reviewer通过之后，再找管理员确认**











