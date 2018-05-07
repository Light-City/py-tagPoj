# -*- coding:utf-8 -*-
# Author:Francis
# 自定义过滤器/标签
from django import template
from django.utils.safestring import mark_safe

register=template.Library() # register名字固定
# 自定义过滤器
@register.filter
def filter_multi(x,y):
    print(x,y) # 12 3   d.age|filter_multi:3  x,y分别对应d.age与filter_multi
    return x*y
# 自定义标签
@register.simple_tag
def simple_tag_multi(x,y,z,p):

    return x*y*z*p