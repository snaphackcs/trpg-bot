from typing import List, Any, Dict
import json



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
    config = open(config_file)
    config = json.loads(config)