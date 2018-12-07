#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
hanlp helper
"""

from HanlpDict import relation_dict, nature_dict


def relation_to_chinese(relation):
    if relation in relation_dict:
        return relation_dict.get(relation)
    else:
        print("relation translate not found ; "+relation)
        return relation


def tag_to_chinese(tag):
    if tag in nature_dict:
        return nature_dict.get(tag)
    else:
        print("tag translate not found ; "+tag)
        return tag
