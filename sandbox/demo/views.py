from django import template
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from django.urls import reverse

from crispy_forms_uikit import __version__ as crispy_uikit_version
from crispy_forms import __version__ as crispy_version
from .forms import FormByFieldsetsForm, FormByTabsForm, FormByAccordionsForm


class CrispyUikitMixin:
    def get_versions(self):
        return {
            "uikit_version": self.kwargs.get('uikit_version', '3.4.0'),
            "django_crispy_forms": crispy_version,
            "crispy_forms_uikit": crispy_uikit_version,
        }

    def get_context_data(self, **kwargs):
        context = super(CrispyUikitMixin, self).get_context_data(**kwargs)
        context.update(self.get_versions())
        return context


class FormContainersMixin:
    def get_success_url(self):
        return reverse('demo:crispy-demo-success', kwargs={
            'uikit_version': self.kwargs.get('uikit_version', '3.4.0')
        })

    def get_form_kwargs(self):
        """
        Pass template pack argument
        """
        kwargs = super(FormContainersMixin, self).get_form_kwargs()
        kwargs.update({
            'pack': "uikit-{}".format(self.kwargs.get('uikit_version', '3.4.0'))
        })
        return kwargs


class FormByFieldsetView(FormContainersMixin, CrispyUikitMixin, FormView):
    template_name = 'crispy_demo/fieldsets.html'
    form_class = FormByFieldsetsForm


class FormByTabView(FormContainersMixin, CrispyUikitMixin, FormView):
    template_name = 'crispy_demo/tabs.html'
    form_class = FormByTabsForm


class FormByAccordionView(FormContainersMixin, CrispyUikitMixin, FormView):
    template_name = 'crispy_demo/accordions.html'
    form_class = FormByAccordionsForm


class StaticPage(FormContainersMixin, CrispyUikitMixin, TemplateView):
    template_name = 'crispy_demo/success.html'
