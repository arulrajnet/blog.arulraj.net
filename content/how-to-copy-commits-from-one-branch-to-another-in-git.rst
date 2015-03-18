How to copy commits from one branch to another in GIT
#####################################################
:date: 2012-01-13 02:16
:author: arul
:category: Programming
:tags: GIT, Linux
:slug: how-to-copy-commits-from-one-branch-to-another-in-git
:status: published

I have GIT version management tool for versioning and using gitolite for
user and project management within git. Will tell about this gitolite
story in a seperate post.

Here we are going to learn how to copy commits from your master to
branch.

Basically I am a linux enthusiast so I will explain everthing here in
commends. Feel free to use git commends :)

-  First you have to check where you are now.

| git branch -a
|  That \* will where you are. Now I am in Master branch.

[caption id="" align="aligncenter" width="349" caption="GIT
Branch"]\ |image0|\ [/caption]

-  Create a new branch and move to that created branch

| git branch <branch\_name>
|  git checkout <branch\_name>

If you are already created branch. No need create branch just git
checkout

-  Once again confirm Are you in correct branch.

git branch -a

-  Pick up the commits to this branch

| git cherry-pick <first\_some\_character\_of\_commit\_hash>
|  Ex: git cherry-pick d1c4b9a5a21e3d09cae

-  How to get the hash tag of commits

git log

[caption id="" align="aligncenter" width="400" caption="GIT
Log"]\ |image1|\ [/caption]

You can get the has tag from here.

-  Then Switch back to master

git checkout master

-  For push this branch to remote server

git push origin <branch\_name>

-  For delete the locally created branch

git branch -D <branch\_name>

.. |image0| image:: http://4.bp.blogspot.com/-cOUKcHXwslk/Tw_aT7ePh7I/AAAAAAAAIy8/8XFZMPUOZhg/s400/git-branch.PNG
   :target: http://4.bp.blogspot.com/-cOUKcHXwslk/Tw_aT7ePh7I/AAAAAAAAIy8/8XFZMPUOZhg/s1600/git-branch.PNG
.. |image1| image:: http://1.bp.blogspot.com/-2vSzYrj_sfk/Tw_nLsAJSGI/AAAAAAAAIzU/k_60_quiZbE/s400/git-log.PNG
   :target: http://1.bp.blogspot.com/-2vSzYrj_sfk/Tw_nLsAJSGI/AAAAAAAAIzU/k_60_quiZbE/s1600/git-log.PNG
