from django.contrib import admin

from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "created", "is_active"]
    list_filter = ["created", "author__username", "category", "is_active"]
    search_fields = ["title", "id", "text", "created"]
    list_editable = ["category", "is_active"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "id"]
    prepopulated_fields = {"slug": ("name",)}
