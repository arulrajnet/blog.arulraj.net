PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
OUTPUTGZIPDIR=$(BASEDIR)/outputgzip
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

FTP_HOST=localhost
FTP_USER=anonymous
FTP_TARGET_DIR=/

SSH_HOST=localhost
SSH_PORT=22
SSH_USER=root
SSH_TARGET_DIR=/var/www

S3_BUCKET=www.arulraj.net
AWS_PROFILE="arulrajnet"

CLOUDFILES_USERNAME=my_rackspace_username
CLOUDFILES_API_KEY=my_rackspace_api_key
CLOUDFILES_CONTAINER=my_cloudfiles_container

DROPBOX_DIR=~/Dropbox/Public/

GITHUB_PAGES_BRANCH=gh-pages

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

SERVER ?= "0.0.0.0"

PORT ?= 0
ifneq ($(PORT), 0)
	PELICANOPTS += -p $(PORT)
endif


help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '   make serve [PORT=8000]              serve site at http://localhost:8000'
	@echo '   make serve-global [SERVER=0.0.0.0]  serve (as root) to $(SERVER):80    '
	@echo '   make devserver [PORT=8000]          serve and regenerate together      '
	@echo '   make devserver-global               regenerate and serve on 0.0.0.0    '
	@echo '   make ssh_upload                     upload the web site via SSH        '
	@echo '   make sftp_upload                    upload the web site via SFTP       '
	@echo '   make rsync_upload                   upload the web site via rsync+ssh  '
	@echo '   make dropbox_upload                 upload the web site via Dropbox    '
	@echo '   make ftp_upload                     upload the web site via FTP        '
	@echo '   make s3_upload                      upload the web site via S3         '
	@echo '   make cf_upload                      upload the web site via Cloud Files'
	@echo '   make github                         upload the web site via gh-pages   '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	bash convert-tags-obsidian-markdown.sh
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

html-debug:
	bash convert-tags-obsidian-markdown.sh
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -v -D --logs-dedup-min-level DEBUG

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve-global:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) -b $(SERVER)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

devserver-global:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS) -b 0.0.0.0

publish:
	bash convert-tags-obsidian-markdown.sh
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

ssh_upload: publish
	scp -P $(SSH_PORT) -r "$(OUTPUTDIR)"/* "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)"

sftp_upload: publish
	printf 'put -r $(OUTPUTDIR)/*' | sftp $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --include tags --cvs-exclude --delete "$(OUTPUTDIR)"/ "$(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)"

dropbox_upload: publish
	cp -r "$(OUTPUTDIR)"/* "$(DROPBOX_DIR)"/

ftp_upload: publish
	lftp ftp://$(FTP_USER)@$(FTP_HOST) -e "mirror -R $(OUTPUTDIR) $(FTP_TARGET_DIR) ; quit"

s3_upload: publish
	python3 output-gzip-compression.py "$(OUTPUTDIR)" "$(OUTPUTGZIPDIR)"
	aws s3 sync "$(OUTPUTGZIPDIR)"/ s3://$(S3_BUCKET)/ --acl public-read --delete --content-type "application/javascript; charset=utf-8" --content-encoding gzip --cache-control max-age=86400 --exclude "*" --include "*.js" --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/ s3://$(S3_BUCKET)/ --acl public-read --delete --content-type "text/css; charset=utf-8" --content-encoding gzip --cache-control max-age=86400 --exclude "*" --include "*.css" --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/ s3://$(S3_BUCKET)/ --acl public-read --delete --content-type "application/xml; charset=utf-8" --content-encoding gzip --exclude "*" --include "*.xml" --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/ s3://$(S3_BUCKET)/ --acl public-read --delete --content-type "text/html; charset=utf-8" --content-encoding gzip --exclude "*" --include "*.html" --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/assets/ s3://$(S3_BUCKET)/assets/ --acl public-read --delete --cache-control max-age=86400 --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/theme/ s3://$(S3_BUCKET)/theme/ --acl public-read --delete --cache-control max-age=86400 --profile $(AWS_PROFILE)
	aws s3 sync "$(OUTPUTGZIPDIR)"/ s3://$(S3_BUCKET) --acl public-read --delete --profile $(AWS_PROFILE)

cf_upload: publish
	cd "$(OUTPUTDIR)" && swift -v -A https://auth.api.rackspacecloud.com/v1.0 -U $(CLOUDFILES_USERNAME) -K $(CLOUDFILES_API_KEY) upload -c $(CLOUDFILES_CONTAINER) .

github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) "$(OUTPUTDIR)"
	git push origin $(GITHUB_PAGES_BRANCH)

.PHONY: html help clean regenerate serve serve-global devserver publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
