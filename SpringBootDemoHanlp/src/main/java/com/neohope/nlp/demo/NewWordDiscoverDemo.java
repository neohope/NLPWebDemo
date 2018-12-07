package com.neohope.nlp.demo;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.corpus.io.IOUtil;
import com.hankcs.hanlp.mining.word.WordInfo;

import java.io.IOException;
import java.util.List;

public class NewWordDiscoverDemo
{
    static final String CORPUS_PATH = "Data/红楼梦/红楼梦.txt";

    public static void main(String[] args) throws IOException
    {
        List<WordInfo> wordInfoList = HanLP.extractWords(IOUtil.newBufferedReader(CORPUS_PATH), 100);
        System.out.println(wordInfoList);
    }
}