# Runner
FastGAL的运行器，用于运行使用FastGAL Editor（暂未开发）编写的Galgame

## 目录结构
- i18n - 国际化json文件存放位置
- res - 游戏资源存放位置（如视频 图片等 通过转换成base64的方式存储在json里）
- scripts - 存放游戏内容json的文件夹 现版本只支持一个game.json
- logs - Runner运行日志
- QtUI - 使用Qt Creator构建的程序UI文件
- logtool - 是FastGAL Runner程序的一部分，用于写日志
## json格式
### config.json
用于存放游戏基本信息以及主菜单布局，Runner目前自带一个编写好的config.json，格式和项的数量是固定的，可以直接在config.json的基础上修改

里面的各种项基本上都能直接看懂，就无需我解释了吧～
### res中的json
用于存放游戏资源如图片、视频，Runner目前自带一个写好的default.json，在res文件夹中，其中包含res/default-unjson/0中的图片。格式就
是给予每个资源一个标签，如1 2 3 company-logo beforce-playing-warning 这些都行，然后在里面写上type（资源类型）和资源的base64就行
，格式固定，项的数量不固定，可以无限制的添加资源，res支持分成多个json，只需要你在引用需要的资源的时候定位到正确的json即可。

举个例子：

在config.json中可以自定义主菜单的按钮贴图，需要开发者给予`imagepath`和`imageindex`这两个参数，比如我NewGame的按钮贴图存在res/def
ault.json里，标签为ohhh，那么我就应该将`imagepath`的值设置为`res/default.json`，并将`imageindex`的值设置为`ohhh`，然而
我正好把res分成了多个json，此时Settings按钮贴图在`res/gameres0.json`里，标签为shhh，那么也是一个道理。

`type`表示资源类型，可以是`image` `video` `voice` `music`
### scripts中的game.json
用于存放游戏内容，比如流程啊，剧情啊，进入主菜单之前要显示什么啊等等等等...`start`和`mainmenu`项中的格式和子项的数量是固定的，但
用于存放游戏基本流程的`story`中的子项数量是非固定的，`story`中会包含`CP0` `CP1`这种子项，大概可以理解为一个个章节，章节内包含的
子项如`0` `1` `2`就是游戏流程了，`type`代表要干什么，例如`text`就是显示剧情文本，`video`就是播放视频。

当`type`为`text`时，`text` `imagepath` `imageindex` `voicepath` `voiceindex` `autotime`项是必须的，分别对应文本内容、
存放此时应出现图片的资源json的位置、图片在资源json中的标签、存放此时需要播放语音的资源json的位置、语音在资源json中的标签、AUTO模式
的文本持续显示时间。如果你并不想在此时显示图片或播放语音，可以直接把图片指向一个全黑图片，把语音指向一个空语音等，总之就是不要留空。

当`type`为`video`时，`videopath` `videoindex`项是必须的，和上面一样，就是存放对应视频的json位置和标签，FastGALRunner暂不支持
提供字幕，所以可以把字幕直接扔进视频里

关于多分支选项的json格式尚未敲定，请等待后续

## 运行Runner
克隆下来然后直接用python3.6或更高版本运行FastGALRunner.py，记得装PySide6

也支持用pyinstaller打包，记得链接mainwindow.py等模块文件