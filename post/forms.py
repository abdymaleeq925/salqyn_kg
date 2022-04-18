from django import forms
from post.models import Comment, Post, Category


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            "comment": forms.TextInput(attrs={
                "class": "form-control"
            })
        }


class PostCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"})
        )

    class Meta:
        model = Post
        fields = ['title', 'image', 'category', 'text', 'is_active']
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-control"})
        }
