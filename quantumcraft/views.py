from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def appointment(request):
    return render(request, 'pages/appointment.html')

def blog(request):
    return render(request, 'pages/blog.html')

def blog_details(request):
    return render(request, 'pages/blog_details.html')

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def pricing(request):
    return render(request, 'pages/pricing.html')

def project(request):
    return render(request, 'pages/project.html')

def service(request):
    return render(request, 'pages/service.html')

def service_details(request):
    return render(request, 'pages/service_details.html')

def team(request):
    return render(request, 'pages/team.html')
