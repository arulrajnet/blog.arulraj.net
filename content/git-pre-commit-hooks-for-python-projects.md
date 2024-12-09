---
title: Git Pre Commit hooks for python projects
date: 2024-11-07 17:55:39
author: arul
category: others
tags: others
slug: git-pre-commit-hooks-for-python-projects
disqus_identifier: git-pre-commit-hooks-for-python-projects
cover: /assets/images/default.png
color: gray
headline: Git Pre Commit hooks for python projects
status: draft
---



```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v4.6.0
  hooks:
    - id: check-yaml
    - id: end-of-file-fixer
    - id: trailing-whitespace
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.6.1
  hooks:
    # Run the linter.
    - id: ruff
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
- repo: https://github.com/Lucas-C/pre-commit-hooks
  rev: v1.5.5
  hooks:
    - id: insert-license
      name: Add license for all Python files
      files: \.py$|\.pyi$
      args:
        - --comment-style
        - "|#|"
        - --license-filepath
        - scripts/license-template.txt
        - --license-filepath
        - scripts/license-template-both.txt
        - --license-filepath
        - scripts/license-template-view.txt
        - --use-current-year
        - --allow-past-years
        - --fuzzy-match-generates-todo
- repo: https://github.com/erskaggs/jira-pre-commit
  rev: v1.0.4
  hooks:
    - id: jira-pre-commit
      stages: [commit-msg]
- repo: local
  hooks:
    - id: pytest
      name: pytest
      entry: ./.venv/bin/coverage
      args:
        - "run"
        - "-m"
        - "pytest"
        - "-vv"
        - "-p no:warnings"
        - "-m not integration"
      pass_filenames: false
      always_run: true
      language: system
      types: [python]
      stages: [pre-push]

    - id: coverage-report
      name: Generate Coverage Report
      entry: ./.venv/bin/coverage
      args:
        - "report"
      language: system
      types: [python]
      stages: [pre-push]

    - id: html-report
      name: Generate HTML Coverage Report
      entry: ./.venv/bin/coverage
      args:
        - "html"
      language: system
      types: [python]
      always_run: true
      stages: [pre-push]
```


https://github.com/executablebooks/mdformat