#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
pyhanlp webdemo
"""

from flask import Flask, request, render_template
from pyhanlp import HanLP, NLPTokenizer
from urllib import parse

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index_page():
    sentence=request.args.get("sentence")
    if sentence is None:
        sentence="习近平指出，中巴建交一年半来，中巴关系强劲起步，我同巴雷拉总统实现互访，双方政治互信日益深化，以共建“一带一路”为牵引，各领域交往合作快速发展，成效显著。事实已经并将继续证明，中巴建交完全正确，惠泽两国人民。无论国际形势如何变化，巩固和发展中巴友好关系是中方坚定不移的外交方针。中方支持巴拿马政府和人民为维护国家安全稳定、改善民生、提升国际影响力所作的努力，支持巴拿马在促进地区经济融合和互联互通方面发挥更大作用。"
    print("/"+sentence)

    terms=HanLP.segment(sentence).__str__()
    keywords=HanLP.extractKeyword(sentence, 2)
    summary = HanLP.extractSummary(sentence, 2)

    sentence_quote = parse.quote(sentence)
    urla = "/dependency_parsing_page?sentence=" + sentence_quote
    urlb = "/dependency_sentence_page?sentence=" + sentence_quote

    message = {
        'sentence':sentence,
        'terms':terms,
        'keywords':keywords,
        'summary':summary,
        'urla': urla,
        'urlb': urlb
    }
    return render_template('index.html',info=message)


@app.route('/dependency_parsing_page', methods=['POST', 'GET'])
def dependency_parsing_page():
    sentence = request.args["sentence"]
    print("/dependency_parsing_page"+sentence)

    """
    需要修改pyhanlp文件，增加一行
    NLPTokenizer=SafeJClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    """
    ann=NLPTokenizer.ANALYZER.analyze(sentence).translateCompoundWordLabels().toStandoff().__str__()
    message = {
            'ann': ann
    }
    return render_template('dependency_parsing.html',info=message)


@app.route('/dependency_sentence_page', methods=['POST', 'GET'])
def dependency_sentence_page():
    sentence = request.args["sentence"]
    print("/dependency_sentence_page>>>"+sentence)
    conll = HanLP.parseDependency(sentence).__str__()
    print(conll)
    message = {
        'conll': conll
    }
    return render_template('dependency_sentence.html',info=message)


@app.route('/segment', methods=['POST', 'GET'])
def segment():
    """
    分词及词性标注
    """
    sentence = request.args["sentence"]
    print("/segment>>>"+sentence)
    terms=HanLP.segment(sentence)
    return terms.__str__()


@app.route('/keyword_extract', methods=['POST', 'GET'])
def keyword_extract():
    """
    关键词提取
    """
    document = request.args["document"]
    print("/keyword_extract>>>"+document)
    keywords = HanLP.extractKeyword(document, 2)
    return keywords.__str__()


@app.route('/summary_extract', methods=['POST', 'GET'])
def summary_extract():
    """
    自动摘要
    """
    document = request.args["document"]
    print("/summary_extract>>>"+document)
    summary=HanLP.extractSummary(document, 2)
    return summary.__str__()


@app.route('/dependency_parsing', methods=['POST', 'GET'])
def dependency_parsing():
    """
    词法分析
    """
    sentence = request.args["sentence"]
    print("/dependency_parsing"+sentence)
    """
    需要修改pyhanlp文件，增加一行
    NLPTokenizer=SafeJClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
    """
    ann=NLPTokenizer.ANALYZER.analyze(sentence).translateCompoundWordLabels()
    return ann.toStandoff().__str__()


@app.route('/dependency_sentence', methods=['POST', 'GET'])
def dependency_sentence():
    """
    句法分析
    """
    sentence = request.args["sentence"]
    print("/dependency_sentence>>>"+sentence)
    conll = HanLP.parseDependency(sentence)
    return conll.__str__()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
