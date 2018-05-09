#!encoding:utf-8
from __future__ import unicode_literals

from colorfield.fields import ColorField
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.db import models

from lib.storage import ImageStorage
from applications.live_streaming.models import Live
from applications.custom_user.models import CustomUser


class Project(models.Model):
	"""项目说明书"""
	name = models.CharField('名称', max_length=50)
	pathwel = models.ImageField('介绍图片', upload_to='project/%Y%m%d', storage=ImageStorage())
	desc = models.TextField('简介', max_length=1000, blank=True, null=True, default='')
	color = ColorField('颜色', max_length=50, default="#00CCFF")

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Project'
		verbose_name = "项目"
		verbose_name_plural = "项目"


class Course(models.Model):
	"""课程"""

	project = models.ForeignKey(Project, verbose_name='归属项目', related_name='Courses', blank=True, null=True)
	lecturer = models.ForeignKey(CustomUser, verbose_name='讲师', related_name='Course_custom_user', blank=True, null=True)
	name = models.CharField('名称', max_length=50)
	pathwel = models.ImageField('介绍图片', upload_to='course/%Y%m%d', storage=ImageStorage(), null=True, blank=True)
	desc = models.TextField('描述', default="", null=True, blank=True)
	sequence = models.PositiveIntegerField('顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")
	update_time = models.DateTimeField("更新时间", auto_now=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Course'
		verbose_name = "课程"
		verbose_name_plural = "课程"
		ordering = ['-update_time']


class Section(models.Model):
	"""课程-章节"""
	course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='所属课程', related_name='Section')
	title = models.CharField('章节标题', max_length=100, default='')
	desc = models.TextField('章节描述', default='', null=True, blank=True)
	sequence = models.PositiveIntegerField('章节顺序', default=1, validators=[MinValueValidator(1)], help_text="默认顺序为1")

	def __unicode__(self):
		return self.title

	class Meta:
		db_table = 'Section'
		verbose_name = "章节"
		verbose_name_plural = "章节"
		ordering = ["course", 'sequence']


class Video(models.Model):
	TYPE = (
		("1", "视频"),
		("2", "考核习题"),
	)
	section = models.ForeignKey(Section, verbose_name='所属章节', related_name='Videos', blank=True, null=True)
	type = models.CharField('类型', max_length=1, choices=TYPE)
	name = models.CharField('视频/习题名称', max_length=255)
	address = models.FileField('视频', upload_to='video/%y%m%d', null=True, blank=True)
	subtitle = models.FileField('字幕', upload_to='video/%y%m%d', null=True, blank=True, default=' ')
	sequence = models.PositiveIntegerField('显示顺序', default=1, validators=[MinValueValidator(1)],
	                                       help_text="从1开始，默认：1")
	duration = models.PositiveIntegerField('总时长(秒)', default=0, help_text="视频成功上传后，由后台补全；单位：秒")
	desc = models.TextField('描述', default='', null=True, blank=True)
	notes = models.TextField('讲师笔记', default='', null=True, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		db_table = 'Video'
		verbose_name = "视频"
		verbose_name_plural = "视频"
		ordering = ["section", 'sequence']


class CommonQuestion(models.Model):
	video = models.ForeignKey(Video, verbose_name="视频", limit_choices_to={'type__in': [1, 2]})
	question = models.CharField(max_length=200, verbose_name='问题')
	answer = models.TextField(verbose_name='回答')

	def __unicode__(self):
		return self.question

	class Meta:
		db_table = 'CommonQuestion'
		verbose_name = "视频常见问题"
		verbose_name_plural = "视频常见问题"
