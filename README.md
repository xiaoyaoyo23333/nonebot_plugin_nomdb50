# nonebot_plugin_nomdb50
# 📝 插件介绍

当用户发送mdb50、moeb50、mdcp stella或mdcp rank时，bot从随机回复池挑选一句进行回复
（偏个人用代码）

# ✨ 功能特点

- 🎯 智能匹配：通过正则表达式精确匹配指定命令
- 💬 引用回复：使用QQ的引用功能回复用户消息
- 🎲 **随机回复：从随机选择
- 📊 日志记录：详细记录触发情况便于调试
- 🛡️ 异常处理：完善的错误处理机制

# 🎯 支持的命令

插件会响应以下命令格式：
- `mdcp stella`
- `mdcp rank`
- `mob50`
- `meb50`

# 🚀 安装方法

# 方法1：直接复制代码
*可以通过 nb-cli 命令创建`你的插件名字`，也可以手动新建空白文件。

1. 在您的 `plugins` 目录下创建新的 Python 文件，如 `__init__.py`
2. 将插件代码复制到该文件中

# 方法2：复制到插件目录
1. 解压压缩包并将文件夹复制到您的 NoneBot2 项目的 `plugins` 目录下
2. 目录结构应该如下：
```
your_bot/
├── plugins/
│   └── nonebot_plugin_nomdb50/
│       └── __init__.py
├── pyproject.toml
└── bot.py
```

# ⚙️ 配置方法

# pyproject.toml 配置
确保您的 `pyproject.toml` 文件包含插件目录配置：

```toml
[tool.nonebot]
plugin_dirs = ["plugins"]
adapters = [
    { name = "OneBot V11", module_name = "nonebot.adapters.onebot.v11" }
]
```


# 🎮 使用示例

# 测试命令
启动机器人后，在QQ中发送以下任意命令：

```
mdcp stella
mdcp rank
mob50
meb50
```

# 预期效果
机器人会：
1. 引用您的消息
2. 随机回复以下消息之一：
   - "我可没有这个功能喔~"
   - "这个功能暂时还没有呢 (＞人＜;)"
   - "诶？这个功能还没实装啦！"
   - ...（共20条可爱回复）

# 🛠️ 自定义配置

# 修改回复内容
编辑插件代码中的 `REPLY_MESSAGES` 列表：

```python
REPLY_MESSAGES = [
    "我可没有这个功能喔~",
    "这个功能暂时还没有呢 (＞人＜;)",
    # 添加您自己的回复...
]
```

# 修改匹配规则
编辑正则表达式来匹配不同的命令：

```python
cmd_notice = on_regex(
    r"\b(?:mdcp\s+(?:stella|rank)|m[oe]b50)\b", 
    priority=10, 
    block=True
)
```

# 调整优先级
修改 `priority` 参数来调整插件的响应优先级（数字越小优先级越高）。

# 🔧 故障排除

# 常见问题

# 1. 插件不响应
- 检查正则表达式是否正确匹配您的命令
- 确认插件已正确加载（查看启动日志）
- 检查是否有其他插件拦截了消息

# 2. 引用功能不工作
- 确认使用的是 OneBot V11 适配器
- 检查QQ客户端是否支持引用功能
- 查看错误日志，插件会自动降级到普通回复

# 3. 随机回复不够随机
- 这是正常现象，Python的随机数生成器可能会出现短期重复
- 可以增加更多回复内容来提高随机性

# 调试方法

# 查看日志
插件会在控制台输出详细日志：
```
[INFO] 用户 12345678 触发功能提示，命令: mdcp stella
```

# 测试正则表达式
可以使用在线正则表达式测试工具验证匹配规则。

# 📈 高级功能

# 添加数据统计
可以扩展插件添加使用统计功能：

```python
# 统计触发次数
trigger_count = {}

@cmd_notice.handle()
async def handle_cmd_notice(event: MessageEvent):
    user_id = event.user_id
    trigger_count[user_id] = trigger_count.get(user_id, 0) + 1
    # ... 其他代码
```

# 添加冷却时间
防止用户频繁触发：

```python
import time

last_trigger = {}

@cmd_notice.handle()
async def handle_cmd_notice(event: MessageEvent):
    user_id = event.user_id
    now = time.time()
    
    if user_id in last_trigger and now - last_trigger[user_id] < 10:  # 10秒冷却
        return
        
    last_trigger[user_id] = now
    # ... 其他代码
```

# 📄 许可证

本插件遵循 MIT 许可证，您可以自由使用、修改和分发。


# 📞 支持

如果您在使用过程中遇到问题，可以：
1. 查看 NoneBot2 官方文档
2. 在相关社区寻求帮助
3. 查看插件日志进行调试

# 作者
xiaoyaoyo_23333
