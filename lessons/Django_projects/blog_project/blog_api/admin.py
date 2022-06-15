from django.contrib import admin

from blog_api.models import Post, Category, PostImages

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(PostImages)
