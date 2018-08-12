from django.contrib import admin
from .models import Post

# Register your models here.
# Tùy biến View Admin
class PostAdmin(admin.ModelAdmin):
	"""docstring for PostAdmin"""
	list_display = ['title', 'date'] 
	list_filter = ['date'] 
	search_fields = ['title']

admin.site.register(Post, PostAdmin)