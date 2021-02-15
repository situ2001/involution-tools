# 卷王的工具 (Early version)

## 想法

学校虽为双非，但卷王肯定不少，由于卷王喜欢知道他人的排名和绩点，所以我就写了这工具(?)

## 使用说明

Note: 目前就只是一个很普通的单功能脚本...

~~我觉得这repo的README用中文写效果更好~~

卷王可以（目前）通过该小工具来：

1. 查询自己的
2. 查询一段的

第一次使用前

``` shell
pip install -r requirements.txt
```

使用方法：

For more detail, please run with `-h` argument.

一般是，先下载后解析，下面是解析一段学号的示例

``` shell
python run.py query --stu-id <你的学号> --query-mode multiple --begin <号段初的学号> --end <号段末的学号>
python run.py parse
```

下载的结果在pdfs文件夹里，目前是下一次删一次。解析的曲线图在result.jpg里。

[![yB4DyT.jpg](https://s3.ax1x.com/2021/02/11/yB4DyT.jpg)](https://imgchr.com/i/yB4DyT)

## TODO

- [x] use `argparse` for better user experience
- [x] single querying
- [ ] more method of parsing the data
- [ ] single querying for others stu_id
- [ ] better logic in run.py
