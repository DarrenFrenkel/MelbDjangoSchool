from django.shortcuts import render

from .models import Post, Comment
# Create your views here.
def blog_posts(request,*args, **kwargs):
	post_list = Post.objects.published()
	template_name = "post_list.html"
	context = {
		"post_list": post_list
	}
	return render(request, template_name, context)

def blog_details(request, slug, *args, **kwargs):
		post = Post.objects.published().get(slug=slug)
		template_name = "blog_details.html"
		context = {
			"post": post
		}
		return render(request, template_name, context)

