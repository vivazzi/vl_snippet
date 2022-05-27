import re

from django.db import models
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from cms.models import CMSPlugin
from django.utils.html import escape

from vl_core.constants import TITLE_HT
from vl_core.fields import TemplateField
from vl_core.template_pool import template_pool


class Snippet(CMSPlugin):
    title = models.CharField(pgettext_lazy('Component title', 'Title'), max_length=200, blank=True, help_text=TITLE_HT)

    content = models.TextField(_('Code or data'), blank=True,
                               help_text=_('You can insert html, javascript code or data, if you use Template'))
    reformed_content = models.TextField(blank=True, editable=False)

    is_video = models.BooleanField(_('Is video?'), default=False,
                                   help_text=_('Select if you want to insert video (from youtube)'))

    tag_id = models.CharField('ID', max_length=100, blank=True, help_text=_('Can be useful for anchor or other tasks'))
    tag_classes = models.CharField(_('Classes'), blank=True, max_length=200,
                                   help_text=_('Separate with blank. It can be useful for adding style to a block '
                                               'if the available classes are known, or simply wrapping it in a tag with any class'))

    template = TemplateField(_('Template'), blank=True)

    def __str__(self):
        res = self.title if self.title else escape(self.content[:50])

        if self.template:
            res += template_pool.obj_template_str(self, res)

        return res

    def save(self, no_signals=False, *args, **kwargs):
        if self.is_video:
            self.reformed_content = ''

            string = re.findall(r'src=".+?"', self.content)
            if string:
                string = string[0]
                url = string[5:-1]
                i = url.find('?')
                if i != -1:
                    url = url[:i]
                self.reformed_content = url
        else:
            self.reformed_content = self.content
        super().save(no_signals, *args, **kwargs)

    class Meta:
        verbose_name = _('Snippet')
        verbose_name_plural = _('Snippets')
