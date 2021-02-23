# 卷王的工具

## 想法

学校虽为双非，但卷王肯定不少，由于卷王喜欢知道他人的排名和绩点，所以我就写了这工具(?)

## 使用说明

~~我觉得这repo的README用中文写效果更好~~

卷王可以（目前）通过该小工具来：

1. 查询自己或他人的
2. 查询一段的绩点并生成csv文件
3. 查询一段的绩点并生成绩点分布图

第一次使用前

``` shell
git clone https://github.com/situ2001/involution-tools.git
cd involution-tools
pip install -r requirements.txt
```

使用方法：

For more details, please run with `-h` argument.

获取某个人的

``` shell
python run.py query --search <学号> --query-mode single
```

获取一段学号的

``` shell
python run.py query --query-mode multiple --begin <号段初的学号> --end <号段末的学号>
python run.py parse --export csv
#or python run.py parse --export csv
```

下载的结果在pdfs文件夹里，目前是下一次删一次。解析的曲线图为`result.jpg`，解析生成的csv为`result.csv`。

## TODO(s)

- [x] ~~use `argparse` for better user experience~~
- [x] ~~single querying~~
- [x] ~~export result to csv~~
- [x] ~~single querying for others stu_id~~
- [ ] refine the logic in run.py
