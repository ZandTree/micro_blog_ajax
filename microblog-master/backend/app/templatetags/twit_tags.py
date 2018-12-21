from django import template
from backend.app.forms import PostForm
register = template.Library()


@register.inclusion_tag('app/snips/_post_form.html')
def post_form():
    form = PostForm()
    return {'form': form}
