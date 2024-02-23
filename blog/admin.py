from django.contrib import admin
from django.utils.html import format_html
from .models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'preview', 'created_at', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title']

    def preview(self, obj):
        return format_html(f"<img width=50 height=50 src='{obj.image.url}'>")


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'name', 'email']
    list_display_links = ['id', 'post']
    search_fields = ['name', 'phone_number']


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
