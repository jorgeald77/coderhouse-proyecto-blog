from django import forms
from django.forms import ModelForm

from blog.models import Post, Category, Profile


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category', 'published', 'author')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'row': 4}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'published': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-select'})
        }


class CategoryCreteForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfileCreateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'name', 'image', 'description', 'url')
        widgets = {
            'user': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 2}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }
