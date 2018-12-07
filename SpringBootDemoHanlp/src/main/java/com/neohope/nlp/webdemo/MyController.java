package com.neohope.nlp.webdemo;

import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import com.hankcs.hanlp.HanLP;
import com.hankcs.hanlp.seg.common.Term;
import com.hankcs.hanlp.tokenizer.NLPTokenizer;


@RestController
public class MyController {
	private static final Logger logger = LoggerFactory.getLogger(MyController.class);  
	
	@Value("${spring.application.name}")
	private String appName;
	
	@RequestMapping("/appName")
	String appName() {
		return appName;
	}
	
	@RequestMapping("/")
	ModelAndView indexPage(ModelAndView mv, @RequestParam(name="sentence",required=false) String sentence){
	    if(sentence==null)sentence="习近平指出，中巴建交一年半来，中巴关系强劲起步，我同巴雷拉总统实现互访，双方政治互信日益深化，以共建“一带一路”为牵引，各领域交往合作快速发展，成效显著。事实已经并将继续证明，中巴建交完全正确，惠泽两国人民。无论国际形势如何变化，巩固和发展中巴友好关系是中方坚定不移的外交方针。中方支持巴拿马政府和人民为维护国家安全稳定、改善民生、提升国际影响力所作的努力，支持巴拿马在促进地区经济融合和互联互通方面发挥更大作用。";
		logger.warn("/"+sentence);

	    String terms=HanLP.segment(sentence).toString();
	    List<String> keywords = HanLP.extractKeyword(sentence, 2);
	    List<String> summary = HanLP.extractSummary(sentence, 2);

	    String sentence_quote="";
		try {
			sentence_quote = URLEncoder.encode(sentence, "utf-8");
		} catch (UnsupportedEncodingException e) {
			e.printStackTrace();
		}
	    String urla = "/dependency_parsing_page?sentence=" + sentence_quote;
	    String urlb = "/dependency_sentence_page?sentence=" + sentence_quote;
	    
	    mv.setViewName("index");
	    mv.addObject("sentence", sentence);
		mv.addObject("terms", terms);
		mv.addObject("keywords", keywords);
		mv.addObject("summary", summary);
		mv.addObject("urla", urla);
		mv.addObject("urlb", urlb);

	    return mv;
	}

	@RequestMapping("/dependency_parsing_page")
	ModelAndView  dependencyParsingPage(ModelAndView mv, @RequestParam(name="sentence",required=false) String sentence){
	    logger.warn("/dependency_parsing_page"+sentence);
	    String ann=NLPTokenizer.ANALYZER.analyze(sentence).translateCompoundWordLabels().toStandoff();
	    mv.setViewName("dependency_parsing");
	    mv.addObject("ann", ann);
	    return mv;
	}

	@RequestMapping("/dependency_sentence_page")
	ModelAndView  dependency_sentence_page(ModelAndView mv, @RequestParam(name="sentence",required=false) String sentence){
		logger.warn("/dependency_sentence_page>>>"+sentence);
	    String conll = HanLP.parseDependency(sentence).toString();
	    mv.setViewName("dependency_sentence");
	    mv.addObject("conll", conll);
	    logger.warn(conll);
	    return mv;
	}

	@RequestMapping("/segment")
	String segment(@RequestParam(name="sentence",required=false) String sentence){
	    //分词及词性标注
		logger.warn("/segment>>>"+sentence);
	    List<Term> terms=HanLP.segment(sentence);
	    return terms.toString();
	}

	@RequestMapping("/keyword_extract")
	String keywordExtract(@RequestParam(name="document",required=false) String document){
	    //关键词提取
	    logger.warn("/keyword_extract>>>"+document);
	    List<String> keywords = HanLP.extractKeyword(document, 2);
	    return keywords.toString();
	}

	@RequestMapping("/summary_extract")
	String summaryExtract(@RequestParam(name="document",required=false) String document){
	    //自动摘要
	    logger.warn("/summary_extract>>>"+document);
	    List<String> summary=HanLP.extractSummary(document, 2);
	    return summary.toString();
	}

	@RequestMapping("/dependency_parsing")
	String dependency_parsing(@RequestParam(name="sentence",required=false) String sentence){
	    //词法分析
	    logger.warn("/dependency_parsing"+sentence);
	    String ann=NLPTokenizer.ANALYZER.analyze(sentence).translateCompoundWordLabels().toStandoff();
	    return ann;
	}

	@RequestMapping("/dependency_sentence")
	String dependency_sentence(@RequestParam(name="sentence",required=false) String sentence){
	    //句法分析
	    logger.warn("/dependency_sentence>>>"+sentence);
	    String conll = HanLP.parseDependency(sentence).toString();
	    return conll;
	}
}
	    