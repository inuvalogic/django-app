from django.contrib import admin

# Register your models here.
from .models import Category, Blog, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_enable']
    @admin.display(
        boolean=True,
        ordering="name",
        description="is Enable?",
    )
    def is_enable(self, obj):
        return obj.enable

# class CommentInline(admin.StackedInline):
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'pub_date', 'was_published_recently']
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="is Recent?",
    )
    def was_published_recently(self, obj):
        return Blog.was_published_recently(obj)
    
    # fields = ["title", "content", "category"]
    fieldsets = [
        (None, {"fields": ["title", "content", "category"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [CommentInline]
    list_per_page = 10
    list_filter = ['pub_date', 'category']
    search_fields = ['title']
    ordering = ['-pub_date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
