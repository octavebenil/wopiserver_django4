#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018-2-10

@author: qi
'''
from django.urls import re_path
from . import views

app_name = 'wopiserver'
urlpatterns = [
    re_path(r'^files/(?P<fileid>[^/]+)$',views.wopiGetFileInfo),
#     re_path(r'^files/(?P<fileid>[^/]+)/$',views.wopiGetFileInfo),
    re_path(r'^files/(?P<fileid>[^/]+)/contents$',views.wopiFileContents),
#     re_path(r'^files/(?P<fileid>[^/]+)/contents/$',views.wopiFileContents),
]

