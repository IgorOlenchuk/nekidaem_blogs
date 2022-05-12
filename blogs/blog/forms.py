from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Post


class PostForm(ModelForm):

    class Meta:

        model = Post
        fields = ["title", "text"]
        labels = {
            'title': _('Заголовок'),
            'text': _('Текст'),
        }
