
from django import template

register = template.Library()

# note: in django 1.4 simple tags will be able to take *args so
# it would be possible for multiple paths to trigger an 'active' page.
# (think a submenu or something similar)
@register.simple_tag(takes_context=True)
def activate(context, path):
    """
    For use in navigation. Returns "active" if the navigation page
    is the same as the page requested.

    The 'django.core.context_processors.request' context processor
    must be activated in your settings.

    In an exception, django doesnt use a RequestContext, so we can't
    necessarily always assume it being present.
    """
    if 'request' in context:
        return bool(context['request'].path == path) and "active" or ""
    return ''
