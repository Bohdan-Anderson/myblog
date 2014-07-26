from django.db import models
from django.contrib import admin
from blogPosts.models import *
from imageManager.models import *
# from itertools import chain





class textInline(admin.StackedInline):
	model = Text
	extra = 0
	# fieldsets = [
	# 	('',{
	# 			'fields':[
	# 				('paragraph',),
	# 				('title','show_title'),
	# 				('subTitle','show_subTitle'),
	# 				('coloum_from','coloum_to','order'),
	# 				('show_on_desktop','show_on_tablet','show_on_mobile'),
	# 				('style')
					
	# 				]
	# 	}),
	# ]


class imageInline(admin.StackedInline):
	model = Image
	extra = 0
	# readonly_fields = ('showImage',)
	# fieldsets = [
	# 	('',{
	# 		'fields':[
	# 			('payload','showImage','alternate_info'),
	# 			('coloum_from','coloum_to','order'),
	# 			('show_on_desktop','show_on_tablet','show_on_mobile',),
	# 			('show_downloader','file_downloader'),
	# 			('style')
	# 		]
	# 	})
	# ]

class postAdmin(admin.ModelAdmin):
	model = Post
	extra = 0
	inlines = [textInline,imageInline]	
	# class Media:
	# 	js = ('/static/js/all-lib.js','/static/js/admin/nicEdit.js','/static/js/admin/admin.js') #
	# 	css = {
	# 		'all': ('/static/css/admin/blog-admin.css',)
	# 	}	

admin.site.register(Post,postAdmin)
admin.site.register(Image)
admin.site.register(Text)

# class visInline(admin.StackedInline):
# 	model = Visualization
# 	extra = 0
# 	readonly_fields = ('feedback_slug','interact_slug','showImage')
# 	fieldsets = [
# 		('',{
# 			'fields':[
# 				('show_title','title'),
# 				('show_subTitle','subTitle'),
# 				('order','coloum_from','coloum_to'),
# 				('data','script'),
# 				('fall_back_image','showImage'),
# 				('interact_box','inter_coloum_from','inter_coloum_to','interact_slug'),
# 				('feedback_box','feed_inter_coloum_from','feed_inter_coloum_to','feedback_slug'),
# 				('style')
# 			]
# 		})
# 	]

# class sectionInline(admin.StackedInline):
# 	model = Section
# 	extra = 0
# 	readonly_fields = ['changeform_link', ]
# 	fieldsets = [('', {
# 						'fields':[
# 							('changeform_link','title','order','coloum_from','coloum_to','coloum_count','show_on_desktop','show_on_tablet','show_on_mobile','style',)]	}),]
# 	def changeform_link(self,instance):
# 		print "test"
# 		print instance
# 		if instance.id:
# 			return u'<a href="/admin/layout/section/%s/" target="_blank">Details</a>' % instance.id
# 		return u'The link is not available till after we save'
# 	changeform_link.allow_tags = True
# 	changeform_link.short_description = 'Link'

# class sectionAdmin(admin.ModelAdmin):
# 	model = Section
# 	extra = 0
# 	readonly_fields = ('showBackground',)
# 	fieldsets = [
# 		('',{
# 			'fields':[('title','show_title','coloum_from','coloum_to','coloum_count','order','subTitle','backgroundImage','showBackground','show_in_sidebar','fullPage','show_on_desktop','show_on_tablet','show_on_mobile','style',)]}
# 		),]
# 	def get_model_perms(self, request):
# 		return {}
# 	inlines = [textInline,imageInline,visInline,sectionInline]
# 	class Media:
# 		js = ('/static/js/all-lib.js','/static/js/admin/nicEdit.js','/static/js/admin/admin.js') #
# 		css = {
# 			'all': ('/static/css/admin/blog-admin.css',)
# 		}

# admin.site.register(Section,sectionAdmin)

# class PageAdmin(admin.ModelAdmin):
# 	inlines = [sectionInline]
# 	readonly_fields = ['showBackground','slug']
# 	fieldsets = [('',
# 					{'fields':[('title','slug','order',),('backgroundImage','showBackground',),'style',]}#'showBackground'
# 				),]
# 	list_display = ('title','order')
# 	list_editable = ('order',)

# admin.site.register(Page,PageAdmin)

# class StyleAdmin(admin.ModelAdmin):
# 	readonly_fields=("slug",)
# 	fieldsets = [('',{'fields':[('title','slug'),'style']}),]

# admin.site.register(Style,StyleAdmin)




# class adminStyle(admin.ModelAdmin):

