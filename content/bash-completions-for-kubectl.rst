:title: Bash completions for kubectl
:slug: bash-completions-for-kubectl
:date: 2016-01-23 12:26:32
:tags: ubuntu, bash-completion
:category: kubernetes
:author: Arul
:lang: en

To install bash completion for your kubectl

Get your kubectl client version

.. code-block:: bash

  kubectl version -c

Get the completion script for the corresponding to your kubectl version.

**Ubuntu**

.. code-block:: bash

  curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/$(kubectl version -c | grep -o -P '(?<=GitCommit:").*(?=",)')/contrib/completions/bash/kubectl | sudo tee /etc/bash_completion.d/kubectl


**Mac**

.. code-block:: bash

  brew install bash-completion
  curl -sSL https://raw.githubusercontent.com/kubernetes/kubernetes/$(kubectl version -c | grep -o -P '(?<=GitCommit:").*(?=",)')/contrib/completions/bash/kubectl > /usr/local/etc/bash_completion.d/kubectl


.. figure:: /assets/images/2016/1/kubectl-bash-completion.png
    :align: center
    :alt: Kubectl Bash completion.
