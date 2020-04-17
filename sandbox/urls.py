"""
Sandbox URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView

urlpatterns = [
    # Dummy homepage just for simple ping view
    path('', TemplateView.as_view(
        template_name="homepage.html"
    ), name='home'),

     path('crispy-forms/', include('sandbox.demo.urls', namespace='demo')),
]

try:
    import debug_toolbar
    urlpatterns += [
        path('__debug__', include(debug_toolbar.urls)),
    ]
except ImportError:
    pass
