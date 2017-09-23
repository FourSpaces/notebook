echo "# tianqibao" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:zaoshu/tianqibao.git

git push origin master


# cd  到指定目录下，添加本地仓库
git init
# 添加文件 到本地仓库
git add README.md
# 提交文件记录
git commit -m "first commit"

# 添加远程仓库
git remote add origin git@github.com:zaoshu/tianqibao.git

# push 到远程
git push origin master