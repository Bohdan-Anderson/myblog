from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from blogPosts.models import Post

# Create your models here.
class Image(models.Model):
	parent = models.ForeignKey(Post)	
	title = models.CharField(max_length=50)
	image = ThumbnailerImageField(upload_to='uploaded/img')
	order = models.IntegerField(default=99)

	def __unicode__(self):
		return self.title