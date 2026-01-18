# coze项目分享

25-26学年秋季学期我接了一个AI在护理实践应用的课程。备课的过程中顺便学了以下工作流怎么搭建，然后我发现AI真的太好用了。这个库放的是一些我平时做的自己觉得用得顺手的东西。相关介绍视频可以去[我的B站这个视频列表](https://www.bilibili.com/video/BV1GbUrBsEPP/)

## 项目列表

1. [日程助手](Workflow-calendar_helper-draft-9238.zip)：给bot发送描述日程的文本或者图片，智能体会自动提取信息，在飞书生成一个日程记录。
2. [kimi输出聊天记录整理器](Workflow-kimi_chat_parser-draft-5263.zip)：将kimi的聊天记录拷贝并发送给工作流，工作流就可以整理成飞书文档。
    - 工作流中涉及到的插件是一个代码节点，可以自己用python写，代码见[这里](codes/kimi_chat_parse.py)