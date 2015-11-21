Shared media files with other users in linux
############################################
:date: 2011-08-18 13:00
:author: arul
:category: Linux
:tags: commands, ubuntu, how to
:slug: shared-media-files-with-other-users-in-linux
:status: published

I think everyone might come across this problem. How to share your Music and Videos with other users in linux machine..? For mine (username is *arul* ) I have all music and videos in my home folder. I want to share those with others ( username is *friends* ) in the same machine. You can ask, by changing the permission of all files with in folder can solve this issue.

Yes you are correct. But this is a partial solution. When you add / create new files with in that folder it have the old permissions. To solve this issue, create / add file with particular permission in that folder. Here is it how to do that.

**First you have create new group. ** This is an optional one, you can use anyone of your old group. For me I created a new group called "media". Assign this group to user whom want you share.

.. code-block:: bash

    sudo groupadd media
    sudo usermod -a -G media friends
    groups friends

In second command option "-a" is important. Then only this group is append to the existing group list otherwise all sub-groups are removed. The final command will display the user is belong to which are the groups. You can also do this using GUI. Goto System → Administration → Users and Groups

|image0| Add new group and assigned to users

Change group to "media" for existing files and folder with in which directory you want to share.

.. code-block:: bash

    sudo chgrp -R media Music/
    sudo chmod g+s -R Music/
    sudo chmod 755 -R Music/

In command "-R" for recursive operations. It will change all folders and subfolders files. Second command for **set group id for Music and sub directory.** Final command for RWX access for user and RX access for group, others for existing files.

Now when you create a new directory with in Music. The "media" group is assigned to that folder. it will look like

.. code-block:: bash

    arul@arul-laptop:~/Music$ mkdir sample
    arul@arul-laptop:~/Music$ ll
    drwxr-sr-x 2 arul media 4096 2011-08-19 00:06 sample

|image1| Music folder list view

Now login as other user. create symbolic link for media folder for easy access.

.. code-block:: bash

    friends@arul-laptop:~/Music$ ln -s /home/arul/Music ./"music on arul"

To know more about File permission view `this <https://help.ubuntu.com/community/FilePermissions>`__ ubuntu help page.

.. |image0| image:: http://3.bp.blogspot.com/-pcMtYOBwgNw/Tk1IGvf9TFI/AAAAAAAAArM/aG_-IY2tIoI/s400/added%2Bnew%2Bgroup.png
   :target: http://3.bp.blogspot.com/-pcMtYOBwgNw/Tk1IGvf9TFI/AAAAAAAAArM/aG_-IY2tIoI/s1600/added%2Bnew%2Bgroup.png
.. |image1| image:: http://4.bp.blogspot.com/-Kyx5kwFVL-c/Tk1eB3TFRKI/AAAAAAAAArU/4F3lIBkXnnc/s400/media%2Bfolder.png
   :target: http://4.bp.blogspot.com/-Kyx5kwFVL-c/Tk1eB3TFRKI/AAAAAAAAArU/4F3lIBkXnnc/s1600/media%2Bfolder.png
