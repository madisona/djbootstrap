from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django import forms
from django.contrib import messages
from django.views.generic import TemplateView, FormView

class SampleForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=200, help_text="Enter your email address", widget=forms.TextInput(attrs={"class": "form-control"}))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "form-control"}))
    hidden_field = forms.CharField(widget=forms.HiddenInput())

class IndexView(FormView):
    form_class = SampleForm

    def form_valid(self, form):
        response = super(IndexView, self).form_valid(form)
        messages.success(self.request, "Thanks! Your fake message went nowhere.")
        return response

    def get_success_url(self):
        return self.request.path

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(
            template_name="sample/index.html"
        ), name='index'),
    url(r'^hero/$', TemplateView.as_view(
        template_name="sample/hero.html"
    ), name='hero'),
    url(r'^container/$', TemplateView.as_view(
        template_name="sample/container.html"
    ), name='container'),
    url(r'^fluid/$', TemplateView.as_view(
        template_name="sample/fluid.html"
    ), name='fluid'),
)
