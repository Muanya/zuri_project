from django.contrib import admin
from .models import Profile, Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'slug', 'status', 'date_created', 'date_modified')
	list_filter = ("status",)
	prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)