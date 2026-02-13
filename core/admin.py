from django.contrib import admin
from .models import Category, Blog

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','created_at']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','author','is_featured','status','created_at']
    prepopulated_fields ={
        "slug":('title',)
    }
    search_fields = ('id','category__category_name','status')
    list_editable = ('is_featured',)    