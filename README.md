<p align="center">
    <img src="./assets/logo/March7th.ico">
</p>

<h1 align="center">
三月七小助手<br>
March7thAssistant
</h1>

崩坏：星穹铁道 自动日常/清体力/锄大地/模拟宇宙/忘却之庭｜图形界面｜消息推送｜循环运行

## 免责声明
本软件是一个外部工具旨在自动化崩坏星轨的游戏玩法。它被设计成仅通过现有用户界面与游戏交互,并遵守相关法律法规。该软件包旨在提供简化和用户通过功能与游戏交互,并且它不打算以任何方式破坏游戏平衡或提供任何不公平的优势。该软件包不会以任何方式修改任何游戏文件或游戏代码。

This software is open source, free of charge and for learning and exchange purposes only. The developer team has the final right to interpret this project. All problems arising from the use of this software are not related to this project and the developer team. If you encounter a merchant using this software to practice on your behalf and charging for it, it may be the cost of equipment and time, etc. The problems and consequences arising from this software have nothing to do with it.

本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。若您遇到商家使用本软件进行代练并收费，可能是设备与时间等费用，产生的问题及后果与本软件无关。


请注意，根据MiHoYo的 [崩坏:星穹铁道的公平游戏宣言](https://sr.mihoyo.com/news/111246?nav=news&type=notice):

    "严禁使用外挂、加速器、脚本或其他破坏游戏公平性的第三方工具。"
    "一经发现，米哈游（下亦称“我们”）将视违规严重程度及违规次数，采取扣除违规收益、冻结游戏账号、永久封禁游戏账号等措施。"

## 功能简介

- **日常**：清体力、每日实训、领奖励、探索派遣、锄大地
- **周常**：历战余响、模拟宇宙、忘却之庭
- 每日实训完成情况支持消息推送
- 凌晨四点或体力恢复后自动启动

> 其中模拟宇宙调用的 [Auto_Simulated_Universe](https://github.com/CHNZYX/Auto_Simulated_Universe) 项目，锄大地调用的 Fhoe-Rail 项目

详情见 [配置文件](assets/config/config.example.yaml) ｜🌟喜欢就点击右上角给个**星星**吧|･ω･) 🌟｜QQ群 [855392201](https://qm.qq.com/q/9gFqUrUGVq) TG群 [点击跳转](https://t.me/+ZgH5zpvFS8o0NGI1)

## 界面展示

![README](assets/screenshot/README1.png)

## 注意事项

- 必须使用PC端 `1920*1080` 分辨率窗口或全屏运行游戏
- 使用锄大地功能，需要安装群文件内提供的补丁包
- 后台运行可以尝试 `远程本地多用户桌面`
- 遇到错误请在 [Issue](https://github.com/moesnow/March7thAssistant/issues) 反馈，提问讨论可以在 [Discussions](https://github.com/moesnow/March7thAssistant/discussions) ，群聊随缘看，欢迎 [PR](https://github.com/moesnow/March7thAssistant/pulls)

## 下载安装

前往 [Releases](https://github.com/moesnow/March7thAssistant/releases/latest) 下载后解压双击 `March7th Assistant.exe` 直接运行

## 更新日志

[Changelog.md](assets/docs/Changelog.md)

## 常见问题

[FQA.md](assets/docs/FQA.md)

## 源码运行

如果你是完全不懂的小白，请通过上面的方式下载安装，不用往下看了。

```cmd
git clone https://github.com/moesnow/March7thAssistant
cd March7thAssistant
pip install -r requirements.txt
python app.py
python main.py
```

---

个人开发不易，如果喜欢本项目，可以微信赞赏送作者一杯咖啡☕

您的支持就是作者开发和维护项目的动力🚀

![sponsor](assets/screenshot/sponsor.jpg)

---

## 相关项目

March7thAssistant 离不开以下开源项目的帮助：

- 模拟宇宙自动化 [https://github.com/CHNZYX/Auto_Simulated_Universe](https://github.com/CHNZYX/Auto_Simulated_Universe)

- OCR文字识别 [https://github.com/hiroi-sora/PaddleOCR-json](https://github.com/hiroi-sora/PaddleOCR-json)

- 图形界面组件库 [https://github.com/zhiyiYo/PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)

## 星光历程

[![星光历程](https://starchart.cc/moesnow/March7thAssistant.svg)](https://starchart.cc/moesnow/March7thAssistant)
