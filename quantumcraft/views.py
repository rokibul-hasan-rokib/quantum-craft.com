from django.shortcuts import render
from core.models import Service, Blog, Team, Category, Tag, Project

def index(request):
    services = Service.objects.filter(is_active=True)[:6]  # Latest 6 services for home
    blogs = Blog.objects.filter(is_published=True)[:3]  # Latest 3 blogs for home
    teams = Team.objects.filter(is_active=True)[:6]  # Latest 6 team members for home
    
    context = {
        'services': services,
        'blogs': blogs,
        'teams': teams,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def appointment(request):
    return render(request, 'pages/appointment.html')

def blog(request):
    blogs = Blog.objects.filter(is_published=True).select_related('category').prefetch_related('tags')
    recent_posts = Blog.objects.filter(is_published=True).order_by('-created_at')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    context = {
        'blogs': blogs,
        'recent_posts': recent_posts,
        'categories': categories,
        'tags': tags,
    }
    return render(request, 'pages/blog.html', context)

def blog_details(request):
    return render(request, 'pages/blog_details.html')

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def project(request):
    projects = Project.objects.filter(is_active=True).select_related('category')
    context = {'projects': projects}
    return render(request, 'pages/project.html', context)

def service(request):
    services = Service.objects.filter(is_active=True)
    context = {'services': services}
    return render(request, 'pages/service.html', context)

def service_details(request):
    return render(request, 'pages/service_details.html')

def team(request):
    teams = Team.objects.filter(is_active=True)
    context = {'teams': teams}
    return render(request, 'pages/team.html', context)
