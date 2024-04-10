from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < Post.MIN_CONTENT_LENGTH:
            raise forms.ValidationError(
                message=f'Your content is too short. The required minimum is {Post.MIN_CONTENT_LENGTH} characters.')
        return content
