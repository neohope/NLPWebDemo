#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
ltp helper
"""

import pyltp as ltp
import os


class LtpHelper:
    def __init__(self):
        # 下载模型文件
        # http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569
        LTP_DATA_DIR = 'Data/ltp_data_v3.4.0/' # ltp模型目录的路径
        cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
        pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
        ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
        par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
        srl_model_path = os.path.join(LTP_DATA_DIR, 'pisrl.model')  # 语义角色标注模型目录路径，模型名称为`pisrl.model`

        self.splitter = ltp.SentenceSplitter

        self.segmentor = ltp.Segmentor()  # 初始化实例
        self.segmentor.load(cws_model_path)  # 加载模型

        self.postagger = ltp.Postagger()  # 初始化实例
        self.postagger.load(pos_model_path)  # 加载模型

        self.recognizer = ltp.NamedEntityRecognizer()  # 初始化实例
        self.recognizer.load(ner_model_path)  # 加载模型

        self.parser = ltp.Parser() # 初始化实例
        self.parser.load(par_model_path)  #加载模型

        self.labeller = ltp.SementicRoleLabeller()  # 初始化实例
        #self.labeller.load(srl_model_path)  # 加载模型, 模型文件有错误

    def __del__(self):
        self.segmentor.release()  # 释放模型
        self.postagger.release()  # 释放模型
        self.recognizer.release()  # 释放模型
        self.parser.release()  # 释放模型
        self.labeller.release()  # 释放模型


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


def ann_coverter(words,postags):
    ann = ''
    sentence = ''
    for i in range(0,len(words)):
        sentence += words[i]+' '

    start=0
    ann += sentence+'\n'
    for i in range(0,len(words)):
        line = 'T' + (i + 1).__str__() + '\t'
        line += postags[i] + '\t'
        line += start.__str__() + '\t'
        start += len(words[i])
        line += start.__str__() + '\t'
        line += words[i]
        ann += line + '\n'
        start += 1

    return ann


def conll_coverter(words, postags, arcs, roles):
    conll = ''
    for i in range(0, len(words)):
        line = (i + 1).__str__() + '\t'
        line += words[i] + '\t'
        line += words[i] + '\t'
        line += postags[i] + '\t'
        # fix me
        #line += roles[i] + '\t'
        line += tag_to_chinese(postags[i]) + '\t'
        line += '-' + '\t'
        line += arcs[i].head.__str__() + '\t'
        line += relation_to_chinese(arcs[i].relation) + '\t'
        line += '-' + '\t'
        line += '-' + '\t'
        conll += line + '\n'

    return conll


if __name__ == '__main__':
    myltp = LtpHelper()
    sentence = "习近平指出，中巴建交一年半来，中巴关系强劲起步，我同巴雷拉总统实现互访，双方政治互信日益深化，以共建“一带一路”为牵引，各领域交往合作快速发展，成效显著。事实已经并将继续证明，中巴建交完全正确，惠泽两国人民。无论国际形势如何变化，巩固和发展中巴友好关系是中方坚定不移的外交方针。"
    words = myltp.segmentor.segment(sentence)  # 分词
    postags = myltp.postagger.postag(words)  # 词性标注
    print(ann_coverter(words,postags))

    arcs = myltp.parser.parse(words, postags) # 依存句法分析
    # roles = myltp.labeller.label(words, postags, arcs)  # 命名实体识别
    # print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
    print(conll_coverter(words, postags, arcs, None))
