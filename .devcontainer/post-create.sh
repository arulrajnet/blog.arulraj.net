#!/usr/bin/env bash
set -ex

##
## Create some aliases
##
echo 'alias ll="ls -alF"' >> $HOME/.bashrc

WORKSPACE_DIR=/workspace
# Change some Poetry settings to better deal with working in a container
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true

# Now install all dependencies
poetry install

# Install these manually due transistive dependencies not handled in python/poetry
pip install awscli==1.33.44
pip install docutils==0.21.2

source .venv/bin/activate

echo "Done!"
