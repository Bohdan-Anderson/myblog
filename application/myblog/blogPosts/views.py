# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404, render
from blogPosts.models import *
from imageManager.models import *
from django.conf import settings

def home(request):
	posts = Post.objects.order_by("created_at").all()
	out = []
	for post in posts:
		subOut = {"parent":post,
				"texts":post.text.order_by('order')
			}
		out.append(subOut);
	return render_to_response('index.html',{"posts":out,"MEDIA_URL":settings.MEDIA_URL})
