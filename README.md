# api-rule-engine
API for sending files to Minereye system and find sensitive information


## Introduction
This repo is meant for sending file to Minereye system and find sensitive information defined by the system

## Technologies
Python 3.7 or higher

## Instalation
pip install api-rule-engine


## Python code example
``` python
from api_rule_engine.client import send_file
file_path = <add local file path>
file_metadata = {'file_name': file_path.split('/')[-1], 'file_path': file_path}
with open(file_path, 'rb') as f:
  res = scan_file(f.read(), file_metadata=file_metadata)

>>> res
{'response_data': {'found_tracking_groups': [{'action_id': '1', 'category_id': '12', 'key': '7',
    'label_id': 'None', 'status': 'added', 'tg_name': 'risk.doc'}]}, 'response_status': 200}

```

## Sending list of files in threads

``` python
import os
import time
import threading
from api_rule_engine.client import scan_file

def scan_file_callback(file_name, file_bytes, file_metadata, fields, return_dict):
    return_dict[file_name] = (scan_file(file_bytes, file_metadata, fields))

## example of files list
file_list = ['../rule_engine/risk.doc', '../rule_engine/1138059831.xls', '../rule_engine/5.xlsx']

def get_bytes(file_path):
    with open(file_path, 'rb') as f:
        return f.read()
## this is 
def simple_metadata(file_path):
    return {'file_name': file_path.split('/')[-1], 'file_path': file_path}

d = {}
threads = []
for file_path in file_list:
    x = threading.Thread(target=scan_file_callback, args=(os.path.basename(file_path), get_bytes(file_path),
                                                          simple_metadata(file_path), {}, d))
    threads.append(x)
for x in threads:
    x.start()
 
 while len(d) < len(file_list):
    time.sleep(1)
  
  print(d)
  {'5.xlsx': {'response_data': {'found_tracking_groups': ''},
  'response_status': 200},
 'risk.doc': {'response_data': {'found_tracking_groups': [{'action_id': '1',
     'category_id': '12',
     'key': '7',
     'label_id': 'None',
     'status': 'added',
     'tg_name': 'risk.doc'}]},
  'response_status': 200},
 '1138059831.xls': {'response_data': {'found_tracking_groups': ''},
  'response_status': 200}}
```
