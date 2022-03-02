# api-rule-engine
API for sending files to Minereye system and find sensitive information


## Introduction
This repo is meant for sending file to Minereye system and find sensitive information defined by the system

## Technologies
Python 3.7 or higher

## Instalation
pip install api-rule-engine


## Python code example
.. code-block:: python

from api_rule_engine.client import send_file
file_path = <add local file path>
file_metadata = {'file_name': file_path.split('/')[-1], 'file_path': file_path}
with open(file_path, 'rb') as f:
  res = scan_file(f.read(), file_metadata=file_metadata)
  print(f'res: {res}')

