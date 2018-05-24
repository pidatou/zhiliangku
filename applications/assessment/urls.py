#!encoding:utf-8
from django.conf.urls import url
from applications.assessment.views import *

urlpatterns = [
	url('^info/$', AssessmentPage.as_view()),
	url('^construct$', ConstructDocker.as_view()),
	url('^result/$', AssessmentResult.as_view()),
	url('^result/info$', AssessmentResultInfo.as_view()),
]
