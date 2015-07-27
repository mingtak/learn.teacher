# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from five import grok
#from learn.teacher import _
#from zope import schema
#from zope.interface import Interface
#from zope.interface import provider
from learn.teacher.interfaces import ITeacher, ICourse
from plone.indexer import indexer
from Products.CMFPlone.utils import safe_unicode


@indexer(ICourse)
@indexer(ITeacher)
def subjects_indexer(obj):
    keywords = []
    for i in obj.subjects:
        keywords.append(safe_unicode(i).encode('utf-8'))
    return keywords
grok.global_adapter(subjects_indexer, name='Subject')

"""
@indexer(ICourse)
def categories_indexer(obj):
    keywords = []
    for i in obj.categories:
        keywords.append(safe_unicode(i).encode('utf-8'))
    return keywords
grok.global_adapter(categories_indexer, name='Subject')
"""
