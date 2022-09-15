from typing import List, Any, Dict
from pprint import pprint
import jsonschema
import json
import os

## =================================
# * self defined modules:
from lib.player import Player

class PaoTuan:
    """
    Paotuan
    ================================
    字段：
    - members/players
        - 类型：list[Player]
        - 功能：记录参与游戏的玩家的状态信息以及id
    - events
        - 类型：list[Event]
        - 功能：储存游戏当中可能出现的事件
    - cards
        - 类型：list[Card]
        - 功能：储存游戏中可用的卡牌类型
    - map
        - 类型：dict[Location]
        - 功能：构建游戏当中的地图结构
    - 其他（要是有的话）
    """

    def __init__(self, players: List[Player], config: str = "/config.json"):
        self.players = {}
        for player in players:
            self.players[player.get_id()] = player

        cfg = load_config(config)
        self.events = cfg["events"]
        self.cards = cfg["cards"]
        self.roles = cfg["roles"]
        self.map = cfg["map"]

    def prepare(self, id: str):
        self.players[id].set_ready()
        pprint(self.players)
        print(self.players[id].is_ready())


def load_config(config_file: str):
    path = os.getcwd()+"/config"
    with open(path+config_file, 'r', encoding='utf-8') as config:
        cfg = json.load(config)

    if not validate(cfg):
        print("Error: invalid configuration file, please try another")
        return {}

    # 如果
    if isinstance(cfg["cards"], str):
        with open(path+cfg["cards"], 'r', encoding='utf-8') as game_cards:
            cfg["cards"] = json.load(game_cards)["cards"]
    if isinstance(cfg["events"], str):
        with open(path+cfg["events"], 'r', encoding='utf-8') as game_events:
            cfg["events"] = json.load(game_events)["events"]
    if isinstance(cfg["roles"], str):
        with open(path+cfg["roles"], 'r', encoding='utf-8') as game_roles:
            cfg["roles"] = json.load(game_roles)["roles"]
    if isinstance(cfg["map"], str):
        with open(path+cfg["map"], 'r', encoding='utf-8') as game_map:
            cfg["map"] = json.load(game_map)["map"]

    return cfg


def validate(cfg):
    path = os.getcwd()+"/config"
    with open(path+cfg["$schema"], 'r', encoding='utf-8') as schema:
        scm = json.load(schema)

    try:
        jsonschema.validate(cfg, scm)
    except:
        print("Oops!!!, failed to validate the configuration")
        return False
    else:
        return True
