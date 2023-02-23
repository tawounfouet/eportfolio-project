from django.contrib import admin
from projects.models import  Project

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



class ProjectAdmin(SummernoteModelAdmin):
    #exclude = ('slug', )
    list_display = ('name', 'active', 'field', ) 
    #list_editable = ('published',)
    #list_display_links = ('id', 'title')
    #search_fields = ('title', )
    #list_per_page = 25
    summernote_fields = ('description', )




admin.site.register(Project, ProjectAdmin) # nous modifions cette ligne, en ajoutant un deuxième argument
