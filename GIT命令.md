[TOC]

#### 初始配置

```
配置所有用户： git config --system [选项]
配置当前用户： git config --global [选项]
配置当前项目： git config  [选项]

配置用户名:sudo git config --system user.name Tedu
配置用户邮箱:git config --global user.email lvze@tedu.cn
配置编译器:git config core.editor pycharm

查看配置信息:git config --list
```

#### 基本命令

```
*初始化仓库:git init
*查看本地仓库状态:git status
*将工作内容记录到暂存区:git add [files..] 或 git add  *
取消文件暂存记录：git rm --cached [file]
*将文件同步到本地仓库：git commit [file] -m [message] 或 git commit  -m 'add files'
查看commit 日志记录：git log 或 git log --pretty=oneline
比较工作区文件和仓库文件差异：git diff  [file]
将暂存区或者某个commit点文件恢复到工作区：git checkout [commit] -- [file]
移动或者删除文件：git  mv  [file] [path] 或 git  rm  [files]
```

#### 版本控制

```
退回到上一个commit节点:git reset --hard HEAD^【一个^表示回退1个版本，依次类推】
退回到指定的commit_id节点：git reset --hard [commit_id]
查看所有操作记录：git reflog
创建标签：git  tag  [tag_name] [commit_id] -m  [message]
查看标签：git tag  【查看标签列表】 或 git show [tag_name]  【查看标签详细信息】
去往某个标签节点：git reset --hard [tag]
删除标签：git tag -d  [tag]
```

#### 保存工作区

```
保存工作区内容:git stash save [message]【将工作区未提交的修改封存，让工作区回到修改前的状态】
查看工作区列表：git stash  list
应用某个工作区：git stash  apply  [stash@{n}]
删除工作区：git stash drop [stash@{n}]  【删除某一个工作区】 或 git stash clear【删除所有保存的工作区】
```

#### 分支管理

```
*查看分支情况:git branch
*创建分支:git branch [branch_name]
*切换工作分支:git checkout [branch]
*创建并切换分支：git checkout -b [branch_name]
*合并分支:git merge [branch]
*删除分支:git branch -d [branch] 【删除分支】 git branch -D [branch]  【删除没有被合并的分支】
```

#### 远程仓库

> 远程主机上的git仓库。实际上git是分布式结构，每台主机的git仓库结构类似，只是把别人主机上的git仓库称为远程仓库。

```
*获取项目:git clone https://github.com/xxxxxxxxx
*获取项目指定分支：git clone -b [分支]	 https://github.com/xxxxxxxxx
*添加远程仓库:git remote  add origin https://github.com/xxxxxxxxx
*查看连接的主机:git remote
*删除远程主机:git remote rm [origin]
*将本地分支推送给远程仓库:git push -u origin [分支]
*推送代码到远程仓库：git push
推送标签:git push origin [tag]【推送本地标签到远程】或git push origin --tags【推送本地所有标签到远程】
推送旧的版本：git push --force origin【用于本地版本比远程版本旧时强行推送本地版本】
删除远程分支和标签：git branch -a【查看所有分支】或git push origin  [:branch]  【删除远程分支】
git push origin --delete tag  [tagname]  【删除远程仓库标签】
*从远程获取代码：git pull
*获取远程指定分支到本地指定分支：git pull [远程路径] [远程分支]:[本地分支] 
*将远程分支master拉取到本地，作为tmp分支：git fetch origin  master:tmp  
```