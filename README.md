# 卷王的工具 （Early version)

## 使用说明

Note: 目前就只是一个很普通的单功能脚本...

~~我觉得这repo用中文写效果更好~~

卷王可以（目前）使用学号段来查询专业的绩点分布，通过这个小工具。

第一次使用前

``` shell
pip install -r requirements.txt
```

使用方法：

先获取该专业的所有绩点再解析生成折线图

``` shell
python rank_download.py <学号> <起始学号> <结束学号>
python rank_parser.py
```

如 `python rank_download.py xxxx 114514 114515`

## TODO

**The area intentionally leaves blank.** (暂时
