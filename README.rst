
DjBootstrap
===========

Helps kickstart your django app using the awesome twitter bootstrap library.

http://getbootstrap.com

As of version 3.0.1 Django 1.5+ is recommended. The sample app will only work with django 1.5+, but the actual
bootstrap stuff should work just fine.


INSTALLATION
------------

::

    >>> pip install djbootstrap

Just add djbootstrap to your INSTALLED_APPS

PROVIDES
--------
**base.html template**

Use it if you feel like it. Just sets up some boilerplate.

**bootstrapped_form template tag**

Renders your form all pretty like using bootstrapped_form.html the bootstrap
css classes and such.

::

    {% load bootstrap_tags %}
    {% bootstrapped_form my_form %}

**notification_center.html**

A simple template snipped to render django's messages output using bootstrap alerts

**Activate Template Tag**

Tells you if the page you're on is the active page.
Requires 'request' context processor

USAGE: ::

    {% url namespace:some_url as the_url %}
    <li class="{% activate the_url %}"><a href="{{ the_url }}"></li>



