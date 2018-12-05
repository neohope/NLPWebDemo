#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
pyltp webdemo
"""

from flask import Flask, request, render_template
from LtpHelper import LtpHelper, ann_coverter, conll_coverter
from urllib import parse


myltp = LtpHelper()
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index_page():
    sentence=request.args.get("sentence")
    if sentence is None:
        sentence="习近平指出，中巴建交一年半来，中巴关系强劲起步，我同巴雷拉总统实现互访，双方政治互信日益深化，以共建“一带一路”为牵引，各领域交往合作快速发展，成效显著。"
    print("/"+sentence)

    words = myltp.segmentor.segment(sentence)  # 分词
    postags = myltp.postagger.postag(words)  # 词性标注
    terms = list(map(lambda x: x[0]+'/'+x[1], zip(words, postags))).__str__()
    netags = '\t'.join(myltp.recognizer.recognize(words, postags))  # 命名实体识别
    arcs = "\t".join("%d:%s" % (arc.head, arc.relation) for arc in myltp.parser.parse(words, postags)) # 依存句法分析
    #roles = ltp.labeller.label(words, postags, arcs).__str__()  # 语义角色标注

    sentence_quote = parse.quote(sentence)
    urla = "/dependency_parsing_page?sentence=" + sentence_quote
    urlb = "/dependency_sentence_page?sentence=" + sentence_quote

    message = {
        'sentence':sentence,
        'terms':terms,
        'netags':netags,
        'arcs':arcs,
        'urla': urla,
        'urlb': urlb
    }
    return render_template('index.html',info=message)


@app.route('/dependency_parsing_page', methods=['POST', 'GET'])
def dependency_parsing_page():
    sentence = request.args["sentence"]
    print("/dependency_parsing_page"+sentence)

    words = myltp.segmentor.segment(sentence)  # 分词
    postags = myltp.postagger.postag(words)  # 词性标注
    ann = ann_coverter(words, postags)
    print(ann)

    message = {
            'ann': ann
    }
    return render_template('dependency_parsing.html',info=message)


@app.route('/dependency_sentence_page', methods=['POST', 'GET'])
def dependency_sentence_page():
    sentence = request.args["sentence"]
    print("/dependency_sentence_page>>>"+sentence)

    words = myltp.segmentor.segment(sentence)  # 分词
    postags = myltp.postagger.postag(words)  # 词性标注
    arc = myltp.parser.parse(words, postags)
    conll = conll_coverter(words, postags, arc, None)
    print(conll)

    message = {
        'conll': conll
    }
    return render_template('dependency_sentence.html',info=message)



@app.route('/sentence_splitter', methods=['POST', 'GET'])
def sentence_splitter(paragraph):
    """
    段落分句
    """
    sentence = request.args["paragraph"]
    print("/paragraph>>>" + paragraph)

    sents = myltp.splitter.split(paragraph)
    return sents


@app.route('/segment', methods=['POST', 'GET'])
def segment():
    """
    分词及词性标注
    """
    sentence = request.args["sentence"]
    print("/segment>>>"+sentence)

    words = myltp.segmentor.segment(sentence)
    postags = myltp.postagger.postag(words)
    terms = list(map(lambda x: x[0]+x[1], zip(words, postags)))
    return terms


@app.route('/named_entity_recognizer', methods=['POST', 'GET'])
def named_entity_recognizer():
    """
    实体识别
    """
    sentence = request.args["sentence"]
    print("/segment>>>"+sentence)

    words = myltp.segmentor.segment(sentence)
    postags = myltp.postagger.postag(words)
    netags = myltp.recognizer.recognize(words, postags)
    return netags


@app.route('/dependency_parsing', methods=['POST', 'GET'])
def dependency_parsing():
    """
    依存句法分析
    """
    sentence = request.args["sentence"]
    print("/dependency_parsing>>>"+sentence)

    words = myltp.segmentor.segment(sentence)
    postags = myltp.postagger.postag(words)
    arcs = myltp.parser.parse(words, postags)
    return arcs


@app.route('/sementic_role_labeller', methods=['POST', 'GET'])
def sementic_role_labeller():
    """
    语义角色标注
    """
    sentence = request.args["sentence"]
    print("/dependency_parsing>>>"+sentence)

    words = myltp.segmentor.segment(sentence)
    postags = myltp.postagger.postag(words)
    arcs = myltp.parser.parse(words, postags)
    roles = myltp.labeller.label(words, postags, arcs)
    return roles


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
