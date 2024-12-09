---
title: Git Pre Commit hooks for golang projects
date: 2024-11-07 17:53:40
author: arul
category: others
tags: others
slug: git-pre-commit-hooks-for-golang-projects
disqus_identifier: git-pre-commit-hooks-for-golang-projects
cover: /assets/images/default.png
color: gray
headline: Git Pre Commit hooks for golang projects
status: draft
---
pre-commit-hooks-for-golang


[turo/pre-commit-hooks: Repo containing custom turo pre-commit hooks](https://github.com/turo/pre-commit-hooks)

[dnephin/pre-commit-golang: Golang hooks for pre-commit](https://github.com/dnephin/pre-commit-golang)

[gogolf-template/.pre-commit-config.yaml at main · iamgoangle/gogolf-template](https://github.com/iamgoangle/gogolf-template/blob/main/.pre-commit-config.yaml)

[securego/gosec: Go security checker](https://github.com/securego/gosec)


license [palantir/go-license: Go tool that applies and verifies that proper license headers are applied to Go files](https://github.com/palantir/go-license)


```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0
  hooks:
    - id: check-yaml
    - id: end-of-file-fixer
    - id: trailing-whitespace
    - id: check-added-large-files
# Formatting, Unit Testing and Cyclomatic Complexity
- repo: https://github.com/dnephin/pre-commit-golang
  rev: v0.5.1
  hooks:
    - id: go-fmt
    - id: go-imports
    - id: no-go-testing
      stages: [pre-push]
    - id: golangci-lint
    - id: go-unit-tests
      stages: [pre-push]
    - id: go-cyclo
    - id: go-critic
# Enforce the commit message have the ticket ID
- repo: https://github.com/erskaggs/jira-pre-commit
  rev: v1.0.4
  hooks:
    - id: jira-pre-commit
      stages: [commit-msg]
# Enforce the best practices for Dockerfile
- repo: https://github.com/hadolint/hadolint
  rev: v2.12.0
  hooks:
    - id: hadolint-docker

```
