from django.shortcuts import render, get_object_or_404
from core.models import Service, Blog, Team, Category, Tag, Project, Testimonial, Brand

def index(request):
    services = Service.objects.filter(is_active=True)[:4]  # First 4 services for home
    blogs = Blog.objects.filter(is_published=True)[:3]  # Latest 3 blogs for home
    teams = Team.objects.filter(is_active=True)[:6]  # Latest 6 team members for home
    testimonials = Testimonial.objects.filter(is_active=True)  # All active testimonials
    brands = Brand.objects.filter(is_active=True)  # All active brands/clients
    projects = Project.objects.filter(is_active=True, is_featured=True)[:6]  # Featured projects for home
    
    context = {
        'services': services,
        'blogs': blogs,
        'teams': teams,
        'testimonials': testimonials,
        'brands': brands,
        'projects': projects,
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

def blog_details(request, slug):
    blog = get_object_or_404(Blog, slug=slug, is_published=True)
    blog.views += 1
    blog.save()
    
    recent_posts = Blog.objects.filter(is_published=True).exclude(id=blog.id).order_by('-created_at')[:5]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    related_posts = Blog.objects.filter(category=blog.category, is_published=True).exclude(id=blog.id)[:3]
    
    context = {
        'blog': blog,
        'recent_posts': recent_posts,
        'categories': categories,
        'tags': tags,
        'related_posts': related_posts,
    }
    return render(request, 'pages/blog_details.html', context)

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

def service_details(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    all_services = Service.objects.filter(is_active=True).exclude(id=service.id)[:6]
    
    context = {
        'service': service,
        'all_services': all_services,
    }
    return render(request, 'pages/service_details.html', context)

def team(request):
    teams = Team.objects.filter(is_active=True)
    context = {'teams': teams}
    return render(request, 'pages/team.html', context)

def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(category=project.category, is_active=True).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'pages/project_details.html', context)
