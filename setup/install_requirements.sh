#!/bin/bash
python --version
pip install --upgrade azureml-sdk
pip install -r requirements.txt
pip install --upgrade azure-cli
pip install snowflake-connector-python
pip install snowflake-snowpark-python
