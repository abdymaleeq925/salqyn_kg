from django import forms
from post.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            "comment": forms.TextInput(attrs={
                "class": "form-control"
            })
        }
