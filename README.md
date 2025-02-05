# Bubbles Valley

[项目地址](https://github.com/segment-tree/bubbles-valley) or [here](https://github.com/segment-tree/pumpking)

## 运行

需要安装 pygame 和 openai 两个包，在项目根目录运行 `python main.py`

 - 特别的，对于 nix 用户，只需 `nix run github:segment-tree/bubbles-valley` （仅在aarch64-linux下测试过，不过应该没问题吧）

## 介绍

这是一个《星露谷》画风的休闲小游戏。小镇镇长的女儿失踪在森林中，等待着勇士的营救。玩家将操纵勇敢的小镇民，通过丢炸弹的方式杀死怪物，穿越迷宫森林，寻找森林深处的她。

## 教程

- 在开始界面按`AD`键或`⬅➡`键进行选项选择，按`enter`键进行确定

- 玩家通过`WASD`键或`⬆⬇⬅➡`键操控角色移动，`F`键与物品交互/开门/开始聊天，开启对话框后按`enter`键继续对话，按`esc`键强制终止对话。与可交流对象对话时可输入英文，按`enter`键确定输入，按`esc`键结束对话。

- 玩家初始生命值为5。玩家可以按`space`键释放炸弹，炸弹将在若干秒后爆炸，形成十字形爆炸范围。角色和怪物被炸弹炸中均会使生命值减1。可摧毁物被炸弹炸中会有概率掉落道具。

- 玩家在商店蓝色柜子前交互即可通过金币购买道具。输入道具序号即可购买。

- 玩家可以与商店女老板聊天或购买道具的方式增加与商店女老板的好感度。当好感度达到一定值时，会达成另一个结局。

- 外挂：按`z`增加玩家移动速度（请不要使速度过快），按`x`减速，按退格键切换是否允许穿墙，按`n`增加金币数量，按`m`反过来，按`c`增加爆炸范围，按`v`反过来，按`b`增加血量，按`scroll lock`使程序崩溃。

- 修改以下 `constants.py` 中的值可以改变部分游戏参数：`AIdecisionEnbled` 值为`True` 时，~~使游戏变卡~~炸毁可摧毁障碍物时掉落物通过ai生成。`LLMavailability` 无法访问校园网时应设为 `False`。`AllowCheat`是否允许上面所说的外挂。`IntialPlayerHp`玩家初始血量。`IntialHp`怪物血量。`DefaultFont`对话框字体。`Keybord*`键位。`Difficulty`适当增加可增加游戏难度（增加商品价格和怪物数量和怪物血量`Difficulty==0`是使用较弱ai）。修改其他值不保证不出bug。`BottomBarMode`玩家血条渲染与否与位置（0不渲染，1渲染在左下角灰色底栏上，2渲染在左上角）

- 游戏理论上会自适应分辨率，如果窗口过大或过小请修改`constants.py` 中的 `CellRatio` 注意要保证其为整数。

- 对于 macOS ，请注意 pygame 有可能把屏幕当1080p分辨率，导致画面有点模糊。对于 linux和macOS 由于使用了不同的字体，对话时字母有可能超出对话框。

- Tips：迷宫森林的出口在地图右上角
