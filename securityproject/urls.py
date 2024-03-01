"""
URL configuration for securityproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#urls.py
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import TemplateView
from securityapp.views import RobotsTxtView, SitemapView
from django.views.static import serve


# def serve_robots_txt(request):
#     print("Serving robots.txt from:", settings.MEDIA_ROOT)
#     return serve(request, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('securityapp.urls')),
    # path(r'^static/(?P<path>.*)$', static,{'document_root': settings.STATIC_ROOT}),
    # path(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    # path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain'))
    # path('robots.txt', RobotsTxtView.as_view(), name='robots_txt'),
    # path('sitemap.xml', SitemapView.as_view(), name='sitemap_xml'),

   
]

print(settings.MEDIA_ROOT)
# exit()

urlpatterns += [
    re_path(r'^robots.txt$', serve, {'document_root': settings.BASE_DIR, 'path': 'robots.txt'}),
    re_path(r'^sitemap.xml$', serve, {'document_root': settings.BASE_DIR, 'path': 'sitemap.xml'}),
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])


# urlpatterns = [
#   re_path(r'^static/(?P<path>.*)$', static,{'document_root': settings.STATIC_ROOT}),
# ]



