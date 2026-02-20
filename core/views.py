from django.shortcuts import render
from .models import Category, Blog

# Create your views here
def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True).order_by('update_at')
    context = {
        'categories':categories,
        'featured_post':featured_post
    }
    return render(request, 'core/home.html', context)