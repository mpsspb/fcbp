import os

from django import template
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


STATIC_PATH = settings.STATICFILES_DIRS[0]
STATIC_URL = settings.STATIC_URL


@register.filter()
def nbsp(value):
    return mark_safe("&nbsp;".join(value.split(' ')))


@register.simple_tag
def static_version(path_string):
    """
    Add modify time of the file
    Use for auto reload by browsers css and js files
    """
    try:
        mtime = os.path.getmtime('%s/%s' % (STATIC_PATH, path_string,))
        return ('%s%s?v=%s' % (STATIC_URL, path_string, mtime,))
    except:
        return path_string
