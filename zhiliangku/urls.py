"""zhiliangku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from zhiliangku import views
from django.conf.urls.static import static
import settings


def callback(request):
    try:
        print request
        print request.GET
        print request.POST
    except:
        import traceback
        traceback.print_exc()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url('^slides/', include('applications.slideshow.urls')),
    url('^tracks/', include('applications.tracks_learning.urls')),
    url('^lives/', include('applications.live_streaming.urls')),
    url('^interview_questions/', include('applications.interview_question.urls')),
    url('^company/', include('applications.company_jobs.urls')),
    url('^customuser/', include('applications.custom_user.urls')),
    url('^polyv/callback', callback),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
