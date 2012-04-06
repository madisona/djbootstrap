
__version__ = '2.0.2'

# default version of Twitter Bootstrap
DEFAULT_VERSION = "2.0.2"
def get_bootstrap_version():
    from django.conf import settings
    return getattr(settings, "BOOTSTRAP_VERSION", None) or "2.0.2"
