## info_metadata:
#### list:
* file_name: str
* file_path: str
* st_mtime: datatime.datetime
* st_atime: datatime.datetime
* create_time: datatime.datetime
* fi_extension: str
* user_name: str (file's owner)
* all_acl: dict, example:
```python 
[{
              "access" : true,
              "identity" : "yaniv.avidan",
              "is_link" : false,
              "type" : "FULL_CONTROL",
              "identity_type" : "CanonicalUser"
            }] 
```
          
