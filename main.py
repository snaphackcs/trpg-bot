from pprint import pprint

from lib import paotuan
from lib.player import Player

def main():
    config = paotuan.PaoTuan([Player("shabi")])
    config.prepare("shabi")

if __name__ == "__main__":
    main()