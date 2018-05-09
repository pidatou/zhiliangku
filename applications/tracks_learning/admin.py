#!encoding:utf-8
from django.contrib import admin

from applications.tracks_learning.model_form import *
from zhiliangku.settings import tinymce_js


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('id', "name", "desc", "pathwel")
	search_fields = ('title',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('id', "project", 'name', "desc", "update_time")
	search_fields = ('name',)

	class Media:
		js = tinymce_js


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ('id', 'course', 'title', 'sequence', "desc")
	search_fields = ("course__name", 'title',)
	form = SectionForm


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ('id', "course", "section", 'name', "type", "address", "subtitle", 'sequence', "duration",)
	search_fields = ("section__title", 'name')
	list_filter = ('type',)

	def course(self, obj):
		if obj.section:
			return obj.section.course.name
		return ""

	course.short_description = "课程"

	class Media:
		js = ['js/webPlugins.js'] + tinymce_js


@admin.register(CommonQuestion)
class CommonQuestionAdmin(admin.ModelAdmin):
	list_display = ('id', "video", "question", 'answer')
	search_fields = ("video__name", 'question')
	form = CommonQuestionForm

	class Media:
		js = tinymce_js
