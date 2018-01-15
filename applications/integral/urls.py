from django.conf.urls import url

import views

urlpatterns = [
    url('^redeem/$', views.Redeem.as_view()),
    url('^all/goods$', views.GetAllGoods.as_view()),
    url('^goods/detail$', views.GoodsDetail.as_view()),
    url('^exchange/records$', views.GetExchangeRecords.as_view()),
    url('^exchange/goods$', views.ExchangeGoods.as_view()),
]