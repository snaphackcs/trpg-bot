from typing import List, Any, Dict
from jsonschema.exceptions import SchemaError, ValidationError

import jsonschema
import json
import os


class PaoTuan:
    """
    Paotuan
    =====================
    
    """
    def __init__(self, member: List[str], config = "config/config.config.json"):
        self.member = member

    def add_member(self, new_member):
        self.member.append(new_member)

def load_config(config_file: str):
    path = os.getcwd()+"/config"
    with open(path+config_file, 'r', encoding='utf-8') as config:
        cfg = json.load(config)
        try:
            validate(cfg)
        except Exception as err:
            print(err.args)
            raise err

        cards

def validate(cfg):
    path = os.getcwd()+"/config"
    with open(path+cfg["$schema"], 'r', encoding='utf-8') as schema:
        scm = json.load(schema)
        try:
            jsonschema.validate(cfg, scm)
        except SchemaError as err:
            raise Exception("Error: %s occur due to\n%s"%(err.message,err.cause))