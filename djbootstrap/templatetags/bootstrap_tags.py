
import urlparse
from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from djbootstrap import get_bootstrap_version

register = template.Library()

# note: in django 1.4 simple tags will be able to take *args so
# it would be possible for multiple paths to trigger an 'active' page.
# (think a submenu or something similar)
@register.simple_tag(takes_context=True)
def activate(context, *paths):
    """
    For use in navigation. Returns "active" if the navigation page
    is the same as the page requested.

    The 'django.core.context_processors.request' context processor
    must be activated in your settings.

    In an exception, django doesnt use a RequestContext, so we can't
    necessarily always assume it being present.
    """
    if 'request' in context:
        return bool(context['request'].path in paths) and "active" or ""
    return ''

@register.simple_tag
def bootstrap(path):
    """
    Returns path to file with static url and bootstrap version
    portions added for you.

    USAGE:

        {% bootstrap "css/bootstrap.min.css" %}

        assuming STATIC_URL = '/static/' and BOOTSTRAP_VERSION = '2.0.2'
        returns "/static/bootstrap/2.0.2/css/bootstrap.min.css"
    """
    version = get_bootstrap_version()
    bootstrap_file = urlparse.urljoin("bootstrap/{0}/".format(version), path)
    return staticfiles_storage.url(bootstrap_file)