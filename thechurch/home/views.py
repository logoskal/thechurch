from django.shortcuts import render
location = 'https://maps.app.goo.gl/QQibjhPHRzZNoBT88'

def home(request):
    return render(request, template_name='home/home.html')

def socials(request):
    return render(request, template_name='home/socials.html')

def about(request):
    return render(request, template_name='home/about.html')

def socials(request):
    return render(request, template_name='home/socials.html')

def socials_button(request):
    return render(request, template_name='home/socials-button.html')

links = """
        http://youtube.com/@EMislene
        
"""