from django.utils.translation import gettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from vl_core.constants import BASIC
from vl_core.forms import TemplateForm
from vl_core.mixins import RenderTemplateMixin
from vl_snippet.models import Snippet


@plugin_pool.register_plugin
class VLSnippetPlugin(RenderTemplateMixin, CMSPluginBase):
    module = BASIC
    model = Snippet
    name = _('Snippet')
    form = TemplateForm
    render_template = 'vl_snippet/snippet.html'
    allow_children = True
    text_enabled = True

    fieldsets = (
        ('', {
            'fields': ('title', 'content', 'is_video', 'template')
        }),
        (_('Additional'), {
            'classes': ('collapse', ),
            'fields': ('tag_id', 'tag_classes')
        })
    )
