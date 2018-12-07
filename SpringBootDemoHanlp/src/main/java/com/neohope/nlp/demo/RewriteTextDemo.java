package com.neohope.nlp.demo;

import com.hankcs.hanlp.dictionary.CoreSynonymDictionary;

public class RewriteTextDemo
{
    public static void main(String[] args)
    {
        String text = "这个方法可以利用同义词词典将一段文本改写成意思相似的另一段文本，而且差不多符合语法";
        System.out.println(CoreSynonymDictionary.rewrite(text));
    }
}