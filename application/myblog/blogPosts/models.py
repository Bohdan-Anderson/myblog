from django.db import models
from django.template.defaultfilters import slugify
import datetime

class Post(models.Model):
	title = models.CharField(max_length = 300)
	order = models.IntegerField(default=99)
	pub_date = models.DateTimeField(auto_now=True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)
	def __unicode__(self):
		return self.title

# Create your models here.
class Text(models.Model):
	parent = models.ForeignKey(Post, related_name='text')
	paragraph = models.TextField()
	pullout = models.BooleanField(default=False)
	code = models.BooleanField(default=False)

	order = models.IntegerField(default=99)
	date_changed = models.DateTimeField(auto_now=True)

	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		datechanged = datetime.datetime.today()
		self.slug = slugify(self.created_at)
		super(Text, self).save(*args, **kwargs)	


