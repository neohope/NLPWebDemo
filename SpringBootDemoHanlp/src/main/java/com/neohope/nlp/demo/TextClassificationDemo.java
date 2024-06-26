package com.neohope.nlp.demo;

import com.hankcs.hanlp.classification.classifiers.IClassifier;
import com.hankcs.hanlp.classification.classifiers.NaiveBayesClassifier;
import com.hankcs.hanlp.classification.corpus.FileDataSet;
import com.hankcs.hanlp.classification.corpus.IDataSet;
import com.hankcs.hanlp.classification.corpus.MemoryDataSet;
import com.hankcs.hanlp.classification.models.NaiveBayesModel;
import com.hankcs.hanlp.classification.statistics.evaluations.Evaluator;
import com.hankcs.hanlp.classification.statistics.evaluations.FMeasure;
import com.hankcs.hanlp.classification.tokenizers.HanLPTokenizer;
import com.hankcs.hanlp.corpus.io.IOUtil;

import java.io.File;
import java.io.IOException;

public class TextClassificationDemo
{
    /**
     * 搜狗文本分类语料库5个类目，每个类目下1000篇文章，共计5000篇文章
     */
    public static final String CORPUS_FOLDER = "Data/搜狗文本分类语料库迷你版";
    /**
     * 模型保存路径
     */
    public static final String MODEL_PATH = "Data/sogou_classification_model.ser";


    private static NaiveBayesModel trainOrLoadModel() throws IOException
    {
        NaiveBayesModel model = (NaiveBayesModel) IOUtil.readObjectFrom(MODEL_PATH);
        if (model != null) return model;

        File corpusFolder = new File(CORPUS_FOLDER);
        if (!corpusFolder.exists() || !corpusFolder.isDirectory())
        {
            System.err.println("没有文本分类语料，请阅读IClassifier.train(java.lang.String)中定义的语料格式与语料下载：" +
                                   "https://github.com/hankcs/HanLP/wiki/%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB%E4%B8%8E%E6%83%85%E6%84%9F%E5%88%86%E6%9E%90");
            System.exit(1);
        }

        IClassifier classifier = new NaiveBayesClassifier(); // 创建分类器，更高级的功能请参考IClassifier的接口定义
        classifier.train(CORPUS_FOLDER);                     // 训练后的模型支持持久化，下次就不必训练了
        model = (NaiveBayesModel) classifier.getModel();
        IOUtil.saveObjectTo(model, MODEL_PATH);
        return model;
    }
    
    private static void predict(IClassifier classifier, String text)
    {
        System.out.printf("《%s》 属于分类 【%s】\n", text, classifier.classify(text));
    }
    
    public static void testA() throws IOException
    {
    	 IClassifier classifier = new NaiveBayesClassifier(trainOrLoadModel());
         predict(classifier, "C罗压梅西内马尔蝉联金球奖 2017=C罗年");
         predict(classifier, "英国造航母耗时8年仍未服役 被中国速度远远甩在身后");
         predict(classifier, "研究生考录模式亟待进一步专业化");
         predict(classifier, "如果真想用食物解压,建议可以食用燕麦");
         predict(classifier, "通用及其部分竞争对手目前正在考虑解决库存问题");
    }
    
    public static void testB() throws IOException
    {
        IDataSet trainingCorpus = new FileDataSet().     // FileDataSet省内存，可加载大规模数据集
        setTokenizer(new HanLPTokenizer()).              // 支持不同的ITokenizer，详见源码中的文档
        load(CORPUS_FOLDER, "UTF-8", 0.9);               // 前90%作为训练集
        IClassifier classifier = new NaiveBayesClassifier();
        classifier.train(trainingCorpus);
        IDataSet testingCorpus = new MemoryDataSet(classifier.getModel()).
        load(CORPUS_FOLDER, "UTF-8", -0.1);              // 后10%作为测试集
        FMeasure result = Evaluator.evaluate(classifier, testingCorpus);   // 计算准确率
        System.out.println(result);
    }
    
    public static void main(String[] args) throws IOException
    {
    	//testA();
    	testB();
    }
}
