# Project in CDK

## Overview

This repo contains the code used to create a simple resume website in AWS S3 using the Python language bindings for the AWS Cloud Development Kit (AWS CDK). 

## Prerequisites

You need to install a fully-functional CDK environment in order to deploy this project:
- AWS CLI installed and configured with credentials to access your AWS account
- NodeJS installed as it is the basis for the CDK
- Python installed as the language binding of choice
- Good Editor -- I used Visual Studio Code and configured the Source Code extension to point to this repo
- You will need to import the S3 and S3_development modules

```bash
source .venv/bin/activate                   # transition into the Python virtual environment
python -m pip install -r requirements.txt   # install base prereqs)
pip install aws-cdk.aws-s3                  # libarary for the S3 resources actions
pip install aws-cdk.aws-s3_deployment       # library for the S3 deployment actions
```
