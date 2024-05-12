from django.contrib import admin
from .models import Category, Post, Like, Region, Agenda


@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'creator']
    list_display_links = ['title']

    prepopulated_fields = {'slug': ['title']}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'creator', 'name', 'description']
    list_display_links = ['name']

    prepopulated_fields = {'slug': ['name']}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'creator', 'views']
    list_display_links = ['title']

    prepopulated_fields = {'slug': ['title']}


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'rating', 'user']
    list_display_links = ['post']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'display_name']
    list_display_links = ['name']