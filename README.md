# 卷王的工具 （Early version)

## 想法

学校虽为双非，但卷王肯定不少，由于卷王喜欢知道他人的排名和绩点，所以我就写了这工具(?)

## 使用说明

Note: 目前就只是一个很普通的单功能脚本...

~~我觉得这repo的README用中文写效果更好~~

卷王可以（目前）使用学号段来查询专业的绩点分布，通过这个小工具。

第一次使用前

``` shell
pip install -r requirements.txt
```

使用方法：

先获取该专业的所有绩点再解析生成折线图

``` shell
python rank_downloader.py <学号> <起始学号> <结束学号>
python rank_parser.py
```

如 `python rank_downloader.py xxxx 114514 114515`

[![yB4DyT.jpg](https://s3.ax1x.com/2021/02/11/yB4DyT.jpg)](https://imgchr.com/i/yB4DyT)

## TODO

**The area intentionally leaves blank.** (暂时
