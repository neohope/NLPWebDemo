package com.neohope.nlp.demo;

import com.hankcs.hanlp.suggest.Suggester;

public class SuggesterDemo
{
    public static void main(String[] args)
    {
    	Suggester suggester = new Suggester();
        String[] titleArray =
        (
                "威廉王子发表演说 呼吁保护野生动物\n" +
                "魅惑天后许佳慧不爱“预谋” 独唱《许某某》\n" +
                "《时代》年度人物最终入围名单出炉 普京马云入选\n" +
                "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散\n" +
                "日本保密法将正式生效 日媒指其损害国民知情权\n" +
                "英报告说空气污染带来“公共健康危机”"
        ).split("\\n");
        for (String title : titleArray)
        {
            suggester.addSentence(title);
        }

        System.out.println(suggester.suggest("陈述", 2));       // 语义
        System.out.println(suggester.suggest("危机公关", 1));   // 字符
        System.out.println(suggester.suggest("mayun", 1));      // 拼音
        System.out.println(suggester.suggest("徐家汇", 1));      // 拼音
    }
}
