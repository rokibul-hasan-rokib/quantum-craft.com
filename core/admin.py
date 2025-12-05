from django.contrib import admin
from .models import Service, Blog, Team, Category, Tag, ProjectCategory, Project


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author_name', 'is_published', 'created_at', 'views']
    list_filter = ['is_published', 'category', 'tags', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']
    ordering = ['-created_at']
    readonly_fields = ['views', 'created_at', 'updated_at']
    filter_horizontal = ['tags']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content')
        }),
        ('Media', {
            'fields': ('thumbnail', 'author_image')
        }),
        ('Categorization', {
            'fields': ('category', 'tags')
        }),
        ('Author & Publishing', {
            'fields': ('author_name', 'read_time', 'is_published')
        }),
        ('Metadata', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'designation']
    list_editable = ['order', 'is_active']
    ordering = ['order', '-created_at']


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'client_name', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['title', 'description', 'client_name']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['order', 'is_active', 'is_featured']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Project Details', {
            'fields': ('client_name', 'project_url', 'completion_date')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )
