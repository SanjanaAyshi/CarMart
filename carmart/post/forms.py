from django import forms
from .models import Post, Comment, CartItem


class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ['account']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class CartForm(forms.ModelForm):
    class Meta:
        model = CartItem
        exclude = ['cart']
