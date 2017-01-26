from fabric.api import *
import fabric.contrib.project as project
import os
import shutil
import sys
import SocketServer

from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
env.cloudfiles_username = 'my_rackspace_username'
env.cloudfiles_api_key = 'my_rackspace_api_key'
env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# s3 bucket name
env.s3_bucket_name = "www.arulraj.net"

# Port for `serve`
PORT = 8000

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

def build():
    """Build local version of site"""
    local('pelican -s pelicanconf.py')

def rebuild():
    """`clean` then `build`"""
    clean()
    build()

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s pelicanconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

def preview():
    """Build production version of site"""
    local('pelican -s publishconf.py')

def cf_upload():
    """Publish to Rackspace Cloud Files"""
    rebuild()
    with lcd(DEPLOY_PATH):
        local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
              '-U {cloudfiles_username} '
              '-K {cloudfiles_api_key} '
              'upload -c {cloudfiles_container} .'.format(**env))

@hosts(production)
def publish():
    """Publish to production via rsync"""
    local('pelican -s publishconf.py')
    project.rsync_project(
        remote_dir=dest_path,
        exclude=".DS_Store",
        local_dir=DEPLOY_PATH.rstrip('/') + '/',
        delete=True,
        extra_opts='-c',
    )

def gh_pages():
    """Publish to GitHub Pages"""
    clean()
    local('pelican -s publishconf.py')
    local("ghp-import -b {github_pages_branch} {deploy_path}".format(**env))
    local("git push origin {github_pages_branch}".format(**env))

def s3_upload():
    clean()
    local('pelican -s publishconf.py')

    local('s3cmd sync {deploy_path}/ s3://{s3_bucket_name}/ --acl-public --delete-removed --mime-type="application/javascript; charset=utf-8" --add-header "Cache-Control: max-age=86400" --exclude "*" --include "*.js"'.format(**env))
    local('s3cmd sync {deploy_path}/ s3://{s3_bucket_name}/ --acl-public --delete-removed --mime-type="text/css; charset=utf-8" --add-header "Cache-Control: max-age=86400" --exclude "*" --include "*.css"'.format(**env))
    local('s3cmd sync {deploy_path}/ s3://{s3_bucket_name}/ --acl-public --delete-removed --mime-type="application/xml; charset=utf-8" --exclude "*" --include "*.xml"'.format(**env))
    local('s3cmd sync {deploy_path}/ s3://{s3_bucket_name}/ --acl-public --delete-removed --mime-type="text/html; charset=utf-8" --exclude "*" --include "*.html"'.format(**env))
    local('s3cmd sync {deploy_path}/assets/ s3://{s3_bucket_name}/assets/ --acl-public --delete-removed --add-header "Cache-Control: max-age=86400" --guess-mime-type'.format(**env))
    local('s3cmd sync {deploy_path}/theme/ s3://{s3_bucket_name}/theme/ --acl-public --delete-removed --add-header "Cache-Control: max-age=86400" --guess-mime-type'.format(**env))
    local('s3cmd sync {deploy_path}/ s3://{s3_bucket_name}/ --acl-public --delete-removed --guess-mime-type'.format(**env))
