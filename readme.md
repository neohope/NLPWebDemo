What is this project about
=========
This is just a pyhanlp demo. 

How to build
============
1. install pythoy 3.6+ x64

2. install packages

```shell
    pip install flask
    pip install pyhanlp
```

3. download pyhanlp data

4. install jdk1.8 x64 and set JAVA_HOME

5. use ide like vscode/pycharm to open the project

6. modify source
```shell
# pyhanlp/__init__.py
# 文件最后，增加一行
NLPTokenizer=SafeJClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
```
7. debug or run

Reference
=========
https://github.com/hankcs/HanLP

https://github.com/hankcs/pyhanlp

http://hanlp.com/
