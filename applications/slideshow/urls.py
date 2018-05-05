#!encoding:utf-8
from django.conf.urls import url

from applications.slideshow.views import *

urlpatterns = [
    url(r'^list$', SlideList.as_view()),
    url(r'^websiteintroduce/list$', WebsiteIntroduceList.as_view()),
    url(r'^recruitmentplan/list$', RecruitmentPlanList.as_view()),
]
