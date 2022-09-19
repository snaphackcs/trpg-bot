# paotuan.py: 一个跑团小bot

[TOC]

----
## 项目结构


----

## 基本类型
### [!TODO] Paotuan
游戏类型，包含所有游戏状态信息以及相关方法。
开始新游戏是通过新建一个Paotuan类来实现的

#### 使用方法
由一名玩家发起游戏，推荐指令为：
```
/trpg start --join 【一组微信名/QQ名】
```
（人数少于3不给开始，且一个人只能发起一次）

游戏会初始化默认剧本并将同意加入的玩家加入到游戏当中。
（玩家利用指令`/trpg join`以确认加入）

---
#### 字段：
- members/players
  - 类型：list[Player]
  - 功能：记录参与游戏的玩家的状态信息以及id
- events
  - 类型：list[Event]
  - 功能：储存游戏当中可能出现的事件
- cards
  - 类型：list[Card]
  - 功能：储存游戏中可用的卡牌类型
- 其他（要是有的话）


### [!TODO] Player


### [!TODO] Card
