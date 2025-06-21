# Markdown-Mathematical-Formula-Syntax-Assistant

项目地址：[Markdown-Mathematical-Formula-Syntax-Assistant](https://github.com/r1ng0rez/Markdown-Mathematical-Formula-Syntax-Assistant)
## 楔子：

最近放假在家没什么事做打算学学Crypto的数学基础，然而在博客上做笔记时经常会遇到MarkDown数学公式语法不知道怎么打的情况，因此我基于Python+Html+JS+CSS开发出了这样一款用于数学公式速查的小工具，如果它帮到了你还请给个star~

## 本地部署
首先把源码clone到本地后，我们需要安装`flask`库
```
git clone https://github.com/r1ng0rez/Markdown-Mathematical-Formula-Syntax-Assistant.git

pip install flask
```
之后运行`main.py`即可，访问你的`localhost:port`就可以啦！
这是此项目的结构：
markdown-formula-cheatsheet/
├── app.py                 # Flask主程序
├── static/                # 静态文件
│   ├── css/
│   │   └── style.css      # 自定义样式
│   └── js/
│       └── script.js      # 自定义JavaScript
└── templates/
    └── index.html         # 主模板文件

## 如何贡献

针对发现的问题以及添加新的公式及公式分类，直接修改并提交 Pull request 即可。

在写新公式时，请复制并修改已有的公式模板
