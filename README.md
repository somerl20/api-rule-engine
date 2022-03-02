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
from api_rule_engine.client import scan_file_callback, get_bytes, 

## example of files list
file_list = ['../rule_engine/risk.doc', '../rule_engine/1138059831.xls', '../rule_engine/5.xlsx']

## this is short example of metadata
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
 {'5.xlsx': {'found_tracking_groups': ''},
 '1138059831.xls': {'found_tracking_groups': ''},
 'risk.doc': {'found_tracking_groups': [{'action_id': '1',
    'category_id': '12',
    'key': '7',
    'label_id': 'None',
    'status': 'added',
    'tg_name': 'risk.doc'}]}}
```

## getting file_metadata
``` python
from api_rule_engine.client import send_file
file_path = '../rule_engine/risk.doc'
file_metadata = {'file_name': file_path.split('/')[-1], 'file_path': file_path}
with open(file_path, 'rb') as f:
    res = scan_file(f.read(), file_metadata=file_metadata, fields=['fi_entities_nested'])
res
{'fi_entities_nested': '[{"display_name": "Email", "id": 10, "values": ["sales@symtrex.com"], "count": 1, "pi_score": 78.9806835921147}, {"display_name": "Full name", "id": 160, "values": ["Lynne Krekeler"], "count": 1, "pi_score": 86.41661304637691}]',
 'found_tracking_groups': [{'action_id': '1',
   'category_id': '12',
   'key': '7',
   'label_id': 'None',
   'status': 'added',
   'tg_name': 'risk.doc'}]}
```

## Full Python API
``` python
scan_file(file_bytes: bytes, file_metadata={}, fields={})
```
file_bytes: files bytes,
file_metadata: dictionary of extra information for finding sensitive information on file
fields: extra metadata to get by request
``` python
scan_file_callback(file_name: str, file_bytes: bytes, file_metadata: dict, fields: list, return_dict: dict)
```
file_name - file name, 
return_dict - dict for returning answer
return_dict : {file_name : answer}
