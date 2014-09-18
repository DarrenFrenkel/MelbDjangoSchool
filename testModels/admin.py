from django.contrib import admin

from .models import Reporter, Article

def full_name(obj):
	return "%s %s" %(obj.first_name.capitalize(), obj.last_name.capitalize())

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('headline', 'updated_date', 'reporter', 'slug')
	list_filter = ('reporter',)


class ArticleInline(admin.TabularInline):
	model = Article
	extra = 1


class ReporterAdmin(admin.ModelAdmin):
	inlines = [ArticleInline,]
	list_display = (full_name, 'email', 'num_of_articles')
	list_display_links = ('email',)
	list_filter = ('num_of_articles',)


admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Article, ArticleAdmin)