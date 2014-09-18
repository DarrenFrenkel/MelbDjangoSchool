from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html

from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	fields = ("published", "title", "content", "slug", "created_at", "show_url")
	list_display = ["title", "published", "updated_at", "created_at", "content"]
	list_display_links = ["title"]
	list_filter = ["published", "updated_at"]
	search_fields = ["title", "content"]
	prepopulated_fields = {"slug": ("title",)}
	readonly_fields = ("show_url",)

	def show_url(self, instance):
		url = reverse("basicblog:blog-details", kwargs={"slug": instance.slug})
		response = format_html("""<a href="{0}">{1}</a>""", url, url)
		return response

	show_url.short_description = "Blog details URL"
	show_url.allow_tags = True

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

# Register your models here.
