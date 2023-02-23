from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from posts.models import BlogPost, AboutMe

"""
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_on', 'last_updated')
    list_editable = ('published',)
"""

class BlogPostAdmin(SummernoteModelAdmin):
    #exclude = ('slug', )
    list_display = ('id', 'title', 'published', 'created_on')
    list_editable = ('published',)
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content', )


admin.site.register(BlogPost, BlogPostAdmin)

admin.site.register(AboutMe, admin.ModelAdmin)


