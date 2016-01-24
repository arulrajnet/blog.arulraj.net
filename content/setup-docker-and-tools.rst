:title: Setup docker and tools
:slug: setup-docker-and-tools
:date: 2016-01-24 06:34:22
:tags: bash_completions, ubuntu
:category: docker
:author: Arul
:lang: en


Guide to install and configure docker and related tools.

Install Docker
--------------

Installing docker on any bash systems.

.. code-block:: bash

  curl -sSL https://get.docker.com/ | sh

Installing bash completions for docker

.. code-block:: bash

  curl -ksSL https://raw.githubusercontent.com/docker/docker/$(docker --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker |sudo tee /etc/bash_completion.d/docker

Docker Tools
------------

**Docker compose**

To install docker-compose

.. code-block:: bash

  sudo apt-get install python-pip
  sudo pip install -U docker-compose

To install bash completions for docker-compose

.. code-block:: bash

  curl -ksSL https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker-compose |sudo tee /etc/bash_completion.d/docker-compose


**Docker alias**

Add this in your ``.bashrc`` file.

.. code-block:: bash

  # ------------------------------------
  # Docker alias and function
  # ------------------------------------

  # Get latest container ID
  alias dl="docker ps -l -q"

  # Get container process
  alias dps="docker ps"

  # Get process included stop container
  alias dpa="docker ps -a"

  # Get images
  alias di="docker images"

  # Get container IP
  alias dip="docker inspect --format '{{ .NetworkSettings.IPAddress }}'"

  # Run deamonized container, e.g., $dkd base /bin/echo hello
  alias dkd="docker run -d -P"

  # Run interactive container, e.g., $dki base /bin/bash
  alias dki="docker run -i -t -P"

  # Execute interactive container, e.g., $dex base /bin/bash
  alias dex="docker exec -i -t"

  # Stop all containers
  dstop() { docker stop $(docker ps -a -q); }

  # Remove all containers
  drm() { docker rm $(docker ps -a -q); }

  # Stop and Remove all containers
  alias drmf='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)'

  # Remove all images
  dri() { docker rmi $(docker images -q); }

  # Dockerfile build, e.g., $dbu tcnksm/test 
  dbu() { docker build -t=$1 .; }

  # Show all alias related docker
  dalias() { alias | grep 'docker' | sed "s/^\([^=]*\)=\(.*\)/\1 => \2/"| sed "s/['|\']//g" | sort; }



Refer from https://github.com/tcnksm/docker-alias/
