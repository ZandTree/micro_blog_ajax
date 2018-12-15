from django import template
from backend.app.forms import PostForm
register = template.Library()

# create a form to render in html

@register.inclusion_tag('app/_post_form.html')
def post_form():
    form = PostForm()
    #variable = YourModel.objects.order_by('-publish')[:5]
    return {'form': form}
