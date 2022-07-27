import random
from datetime import date
from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.rule import keyword
from nonebot.adapters.onebot.v11 import MessageSegment, GroupMessageEvent, Message


def baoyan_school(rank):
	list1 = ["清华大学", "北京大学"]
	list2 = ["中科院计算所", "中科院软件所", "中国人民大学", "中国科学技术大学", "南京大学", "浙江大学", "复旦大学", "上海交通大学"]
	list3 = ["北京航空航天大学", "北京邮电大学", "中山大学", "同济大学", "西安交通大学", "天津大学", "南开大学", "武汉大学", "华中科技大学", "东南大学", "华东师范大学",
	         "哈尔滨工业大学"]
	if (rank <= 3):
		return (random.choice(list1), "你给我回来😭😭😭")
	elif (rank <= 8):
		return (random.choice(list2), "你给我回来😭😭😭")
	elif (rank <= 15):
		return (random.choice(list3), "感觉还行捏🤭🤭🤭")
	elif (rank <= 40):
		return ("北京邮电大学", "哈哈，又要在你邮待三年了捏🤗🤗🤗")


baoyan_rule = keyword("保研")
baoyan = on_keyword(["反卷斗士"], rule=baoyan_rule, priority=15)


@baoyan.handle()
async def baoyan_handle(bot: Bot, event: Event):
	rank = random.choice(range(1, 150))
	if event.get_user_id() in ["1317794623"]:
		rank = 1
	if event.get_user_id() in ["1798508303"]:
		rank = random.choice(range(1, 40))
	msg = ""
	if rank <= 40:
		school, description = baoyan_school(rank)
		if school == "华中科技大学":
			description = "咋的，你也是精神华科人是吧😠😠😠"
		msg += "你以全年级{}/150的排名成功保研到{}，{}".format(rank, school, description)
	else:
		msg += "你在全年级排在了第{}/150名，咱还是准备好好考研上岸吧😰😰😰".format(rank)
	await baoyan.finish(Message(f'[CQ:at,qq={event.get_user_id()}] ' + msg))
