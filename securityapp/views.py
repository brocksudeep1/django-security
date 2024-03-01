# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print(request)
    # exit()
    # response = HttpResponse("Hello, Django!")
    return render(request, 'securityapp/example.html')



from django.http import HttpResponse
from django.views import View
from django.conf import settings
import os

class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        robots_txt_path = os.path.join(settings.BASE_DIR, 'robots.txt')
        
        with open(robots_txt_path, 'r') as file:
            content = file.read()

        return HttpResponse(content, content_type='text/plain')


class SitemapView(View):
    def get(self, request, *args, **kwargs):
        sitemap_path = os.path.join(settings.BASE_DIR, 'sitemap.xml')
        
        with open(sitemap_path, 'r') as file:
            content = file.read()

        return HttpResponse(content, content_type='application/xml')