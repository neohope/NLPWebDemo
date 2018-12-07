package com.neohope.nlp.demo;


import com.hankcs.hanlp.mining.cluster.ClusterAnalyzer;

public class TextClusteringDemo {
	 /**
     * 搜狗文本分类语料库5个类目，每个类目下1000篇文章，共计5000篇文章
     */
    public static final String CORPUS_FOLDER = "Data/搜狗文本分类语料库迷你版";
    
	private static void testA()
	{
        ClusterAnalyzer<String> analyzer = new ClusterAnalyzer<String>();
        analyzer.addDocument("赵一", "流行, 流行, 流行, 流行, 流行, 流行, 流行, 流行, 流行, 流行, 蓝调, 蓝调, 蓝调, 蓝调, 蓝调, 蓝调, 摇滚, 摇滚, 摇滚, 摇滚");
        analyzer.addDocument("钱二", "爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲");
        analyzer.addDocument("张三", "古典, 古典, 古典, 古典, 民谣, 民谣, 民谣, 民谣");
        analyzer.addDocument("李四", "爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 爵士, 金属, 金属, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲, 舞曲");
        analyzer.addDocument("王五", "流行, 流行, 流行, 流行, 摇滚, 摇滚, 摇滚, 嘻哈, 嘻哈, 嘻哈");
        analyzer.addDocument("马六", "古典, 古典, 古典, 古典, 古典, 古典, 古典, 古典, 摇滚");
        System.out.println(analyzer.kmeans(3));
        System.out.println(analyzer.repeatedBisection(3));
        System.out.println(analyzer.repeatedBisection(1.0)); // 自动判断聚类数量k
	}
	
	private static void testB()
	{
		for (String algorithm : new String[]{"kmeans", "repeated bisection"})
        {
            System.out.printf("%s F1=%.2f\n", algorithm, ClusterAnalyzer.evaluate(CORPUS_FOLDER, algorithm) * 100);
        }
	}
	
	public static void main(String[] args)
	{
		testA();
		testB();
	}
}
