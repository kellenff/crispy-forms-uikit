"""
Urls for "crispy form uikit" demo
"""
from django.urls import path

from .views import FormByFieldsetView, FormByTabView, FormByAccordionView, StaticPage

app_name = 'demo'

urlpatterns = [
    path('uikit/',
         FormByFieldsetView.as_view(),
         name='crispy-demo-form-fieldsets'),
    path('uikit/fieldsets/',
         FormByFieldsetView.as_view(),
         name='crispy-demo-form-fieldsets'),
    # path('uikit/tabs/',
    #      FormByTabView.as_view(),
    #      name='crispy-demo-form-tabs'),
    # path('uikit/accordions/',
    #      FormByAccordionView.as_view(),
    #      name='crispy-demo-form-accordions'),
    # path('uikit/success/',
    #      StaticPage.as_view(),
    #      name='crispy-demo-success'),
]
