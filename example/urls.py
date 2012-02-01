from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(
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
