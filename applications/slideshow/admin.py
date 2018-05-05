#!encoding:utf-8
from django.contrib import admin

from applications.slideshow.model_form import *


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "category", "video", "sequence", "desc", 'pathwels')
    search_fields = ('name',)
    list_filter = ('category',)
    form = CarouselForm

    def pathwels(self, obj):
        return '<img src="%s" height="24" width="24" />' % (obj.pathwel.url)

    pathwels.allow_tags = True
    pathwels.short_description = "轮播图片"


@admin.register(WebsiteIntroduce)
class WebsiteIntroduceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "sequence", "desc", 'pathwels')
    search_fields = ('title',)

    def pathwels(self, obj):
        return '<img src="%s" height="24" width="24" />' % (obj.pathwel.url)

    pathwels.allow_tags = True
    pathwels.short_description = "介绍图片"


@admin.register(RecruitmentPlan)
class RecruitmentPlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "sequence", "desc")
    search_fields = ('title',)
