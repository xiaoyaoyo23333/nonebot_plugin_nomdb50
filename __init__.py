from nonebot.plugin import PluginMetadata
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Message, MessageSegment, MessageEvent
from nonebot.log import logger
import random

__plugin_meta__ = PluginMetadata(
    name="nomdb50",
    description="当用户请求特定功能时给予随机提示回复",
    usage="自动触发，支持命令：mdcp stella, mdcp rank, mdb50, moeb50",
    type="application",
    homepage="https://github.com/xiaoyaoyo23333/nonebot_plugin_nomdb50",
    supported_adapters={"~onebot.v11"},
)

# 扩展的随机回复池
REPLY_MESSAGES = [
        "Atri n_(づ︶ど) 可没有这个功能喔~",
    "这个功能暂时还没有呢 (＞人＜;)",
    "诶？这个功能还没实装啦！",
    "抱歉呢，这个功能还在开发中~",
    "这个功能...Atri n_(づ︶ど) 还没有学会呢 (´･_･`)",
    "主人还没教Atri n_(づ︶ど) 这个功能啦！",
    "这个功能...或许未来会有？",
    "Atri n_(づ︶ど) 暂时无法提供这个服务呢 (。-ω-)zzz",
    "功能不存在哦，要不要试试别的？",
    "emmm...这个Atri n_(づ︶ど) 真的不会诶 (╯︵╰)",
    "你是不是在为难Atri n_(づ︶ど) (´•̥̥̥ω•̥̥̥`)",
    "技能点还没点到这里啦 ╮(╯_╰)╭",
    "要不教教Atri n_(づ︶ど) 怎么做？(๑•̀ㅂ•́)و✧",
    "Atri n_(づ︶ど) 的能力还没覆盖到这里呢 (´∀｀)"
]

# 正则匹配：mdcp stella / mdcp rank / mob50 / meb50
cmd_notice = on_regex(
    r"\b(?:mdcp\s+(?:stella|rank)|mdb50|moeb50)\b", 
    priority=5, 
    block=True
)

@cmd_notice.handle()
async def handle_cmd_notice(event: MessageEvent):
    """处理功能提示请求"""
    # 记录触发日志
    user_id = event.user_id
    message_text = str(event.message).strip()
    logger.info(f"用户 {user_id} 触发功能提示，命令: {message_text}")
    
    # 随机选择回复消息
    reply_text = random.choice(REPLY_MESSAGES)
    
    # 构造回复消息（引用+文本合并为一条消息）
    await cmd_notice.finish(
        MessageSegment.reply(event.message_id) + 
        MessageSegment.text(reply_text)
    )
