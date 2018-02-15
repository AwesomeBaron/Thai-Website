from django import forms
from .models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'image']

    def clean(self):
        title = self.cleaned_data['title']

        check = Post.objects.get(title__iexact=title)
        if check:
            raise forms.ValidationError('A post with that \
            title already exist')

        return title