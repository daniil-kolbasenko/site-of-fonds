from django.shortcuts import render
from .models import MenuItem, SiteSettings

def get_site_context():
    settings = SiteSettings.objects.first()
    if not settings:
        settings = SiteSettings.objects.create()
    
    menu_items = MenuItem.objects.filter(is_active=True)
    
    return {
        'site_settings': settings,
        'menu_items': menu_items,
    }

def index(request):
    context = get_site_context()
    context['page_title'] = 'Главная'
    return render(request, 'foundation/index.html', context)

def about(request):
    context = get_site_context()
    context['page_title'] = 'О фонде'
    return render(request, 'foundation/index.html', context)

def program(request):
    context = get_site_context()
    context['page_title'] = 'Программа'
    return render(request, 'foundation/index.html', context)

def patient_stories(request):
    context = get_site_context()
    context['page_title'] = 'Истории пациентов'
    return render(request, 'foundation/index.html', context)

def support(request):
    context = get_site_context()
    context['page_title'] = 'Поддержать'
    return render(request, 'foundation/index.html', context)