package com.neohope.nlp.refn;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class HanlpHelper {
	private static final Logger logger = LoggerFactory.getLogger(HanlpHelper.class);  

	public String relationToChinese(String relation){
	    if(HanlpDict.relationDict.containsKey(relation)){
	    	return HanlpDict.relationDict.get(relation);
	    }
	    else{
	        logger.warn("relation translate not found ; "+relation);
	        return relation;
	    }
	}

	public String tagToChinese(String tag){
		if(HanlpDict.natureDict.containsKey(tag)){
	        return HanlpDict.natureDict.get(tag);
		}
	    else{
	        logger.warn("tag translate not found ; "+tag);
	        return tag;
	    }
	}
	
}
    
