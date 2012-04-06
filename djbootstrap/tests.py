
from django import template
from django import test

import djbootstrap
from djbootstrap.templatetags import bootstrap_tags

__all__ = (
    'GetBootstrapVersionTests',
    'TemplateTagTests',

)

class GetBootstrapVersionTests(test.TestCase):

    def test_gets_bootstrap_version_from_settings(self):
        with self.settings(BOOTSTRAP_VERSION="0.1.4"):
            self.assertEqual("0.1.4", djbootstrap.get_bootstrap_version())

    def test_gets_default_bootstrap_version(self):
        with self.settings(BOOTSTRAP_VERSION=None):
            self.assertEqual(djbootstrap.DEFAULT_VERSION, djbootstrap.get_bootstrap_version())


class TemplateTagTests(test.TestCase):

    def test_bootstrap_tag(self):
        with self.settings(BOOTSTRAP_VERSION="2.0.2", STATIC_URL="/static/"):
            url = bootstrap_tags.bootstrap("css/bootstrap.min.css")
            self.assertEqual("/static/bootstrap/2.0.2/css/bootstrap.min.css", url)

    def test_bootstrap_tag_in_template(self):
        t = template.Template("""
            {% load bootstrap_tags %}

            <link href="{% bootstrap 'css/bootstrap.css' %}" rel="stylesheet" type="text/css">
        """)

        expected_result = '<link href="/static/bootstrap/2.0.2/css/bootstrap.css" rel="stylesheet" type="text/css">'
        self.assertHTMLEqual(expected_result, t.render(template.Context({})))

    def test_active_when_path_matches_request_path(self):
        request = test.RequestFactory().get('/my/path/')
        context = template.RequestContext(request)

        result = bootstrap_tags.activate(context, request.path)
        self.assertEqual("active", result)

    def test_active_when_request_path_one_of_paths(self):
        request = test.RequestFactory().get('/blog/post/two/')
        context = template.RequestContext(request)

        result = bootstrap_tags.activate(context, '/blog/post/', '/blog/post/two/')
        self.assertEqual("active", result)

    def test_not_active_when_request_path_not_in_paths(self):
        request = test.RequestFactory().get('/some-path/')
        context = template.RequestContext(request)

        result = bootstrap_tags.activate(context, '/blog/post/', '/blog/post/two/')
        self.assertEqual("", result)

    def test_returns_empty_string_when_doesnt_have_request_context(self):
        context = template.Context({})
        result = bootstrap_tags.activate(context, "/")
        self.assertEqual("", result)

    def test_returns_active_when_request_is_same_path(self):
        t = template.Template("""
            {% load bootstrap_tags %}

            <a href="/my/path/" class="{% activate '/my/path/' %}">Nav Tab</a>
        """)
        request = test.RequestFactory().get('/my/path/')
        context = template.RequestContext(request)
        response = t.render(context)
        self.assertEqual('<a href="/my/path/" class="active">Nav Tab</a>', response.strip())

    def test_returns_empty_string_when_nav_tab_is_not_current_request(self):
        t = template.Template("""
            {% load bootstrap_tags %}

            <a href="/home/page/" class="{% activate '/home/page/' %}">Nav Tab</a>
        """)
        request = test.RequestFactory().get('/other/path/')
        context = template.RequestContext(request)
        response = t.render(context)
        self.assertEqual('<a href="/home/page/" class="">Nav Tab</a>', response.strip())


