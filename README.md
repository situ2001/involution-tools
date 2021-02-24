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
# 单人
python run.py query --search <学号>

# 多人
python run.py query --begin <号段初的学号> --end <号段末的学号>

# 获取完后顺便解析的话，直接后面加 --export csv 如下
python run.py query --begin <号段初的学号> --end <号段末的学号> --export csv

# 解析./pdfs文件夹里面的已下载文件
python run.py parse --export csv 
# 或
python run.py parse --export jpg
```

下载的结果在pdfs文件夹里，目前是下一次删一次。解析的曲线图为`result.jpg`，解析生成的csv为`result.csv`。
