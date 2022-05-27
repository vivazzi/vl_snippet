from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class SnippetConfig(AppConfig):
    name = 'vl_snippet'
    verbose_name = _('Snippet')
