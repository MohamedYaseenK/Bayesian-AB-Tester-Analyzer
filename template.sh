#!/bin/bash
set -e

PROJECT_NAME="ab-tester"

mkdir -p $PROJECT_NAME/{data/raw,data/adapters,core/bayesian,core/validity,api,app,tests}

touch $PROJECT_NAME/data/adapters/__init__.py
touch $PROJECT_NAME/data/adapters/meututor_adapter.py

touch $PROJECT_NAME/core/__init__.py
touch $PROJECT_NAME/core/schema.py
touch $PROJECT_NAME/core/verdict.py

touch $PROJECT_NAME/core/bayesian/__init__.py
touch $PROJECT_NAME/core/bayesian/beta_binomial.py
touch $PROJECT_NAME/core/bayesian/gamma_poisson.py
touch $PROJECT_NAME/core/bayesian/normal_normal.py

touch $PROJECT_NAME/core/validity/__init__.py
touch $PROJECT_NAME/core/validity/srm_check.py

touch $PROJECT_NAME/api/__init__.py
touch $PROJECT_NAME/api/main.py

touch $PROJECT_NAME/app/dashboard.py

touch $PROJECT_NAME/tests/__init__.py

touch $PROJECT_NAME/requirements.txt
touch $PROJECT_NAME/.gitignore
touch $PROJECT_NAME/README.md

cd $PROJECT_NAME
git init -q

echo "Scaffold created at ./$PROJECT_NAME"