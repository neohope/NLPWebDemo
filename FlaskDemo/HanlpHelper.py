#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
hanlp helper
"""


def relation_to_chinese(relation):
    mydict = {"ATT": "定中关系",
              "QUN": "数量关系",
              "COO": "并列关系",
              "APP": "同位关系",
              "LAD": "前附加关系",
              "RAD": "后附加关系",
              "RIM": "比拟关系",
              "VOB": "动宾关系",
              "SBV": "主谓关系",
              "POB": "介宾关系",
              "MT": "语态结构",
              "IS": "独立结构",
              "CMP": "动补结构",
              "ADV": "状中结构",
              "VV": "联动结构",
              "CNJ": "关联结构",
              "IC": "独立分句",
              "DC": "依存分句",
              "DE": "的",
              "DI": "地",
              "DEI": "得",
              "BA": "把",
              "BEI": "被",
              "WP": "标点符号"}

    if relation in mydict:
        return mydict.get(relation)
    else:
        print("relation translate not found ; "+relation)
        return relation


def tag_to_chinese(tag):
    mydict = {"a": "形容词",
              "b": "其他名词修饰语",
              "c": "连接词",
              "d": "副词",
              "e": "感叹词",
              "g": "语素",
              "h": "前缀",
              "i": "成语",
              "j": "缩写",
              "k": "后缀",
              "m": "数词",
              "n": "名词",
              "nd": "方位名词",
              "nh": "人名",
              "ni": "机构名",
              "nl": "方位名词",
              "ns": "地名",
              "nt": "时间",
              "nz": "专有名词",
              "o": "拟声词",
              "p": "介词",
              "q": "量词",
              "r": "代名词",
              "u": "助词",
              "v": "动词",
              "wp": "符号",
              "ws": "外来名词",
              "x": "非词位"}

    if tag in mydict:
        return mydict.get(tag)
    else:
        print("tag translate not found ; "+tag)
        return tag


def ne_to_chinese(ne):
    mydict = {"Nm": "数词",
              "Ni": "机构名",
              "Ns": "地名",
              "Nh": "人名",
              "Nt": "时间",
              "Nr": "日期",
              "Nz": "专有名词"}

    if ne in mydict:
        return mydict.get(ne)
    else:
        print("ne translate not found ; "+ne)
        return ne
