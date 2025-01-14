from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
  class Meta:
    model = Post
    fields = ['url', 'body', 'tags']
    labels = {
      'body' : 'Caption',
      'tags' : 'Category',
    }
    widgets = {
      'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a caption...'}),
      'url' : forms.TextInput(attrs={'placeholder': 'Add url...'}),
      'tags' : forms.CheckboxSelectMultiple(),
    }
    
class PostEditForm(ModelForm):
  class Meta:
    model = Post
    fields = ['body', 'tags']
    labels = {
      'body' : '',
      'tags' : 'Category',
    }
    widgets = {
      'body' : forms.Textarea(attrs={'rows' : 3, 'class' : 'text-lg rounded-lg'}),
      'tags' : forms.CheckboxSelectMultiple(attrs={'class': 'my-4'}),
    }
    
class CommentCreateForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['body']
    widgets = {
      'body': forms.TextInput(attrs={'placeholder': 'Add comment...', 'class': '!text-sm'})
    }
    labels = {
      'body': ''
    }
    
class ReplyCreateForm(ModelForm):
  class Meta:
    model = Reply
    fields = ['body']
    widgets = {
      'body': forms.TextInput(attrs={'placeholder': 'Add reply...', 'class': '!text-sm'})
    }
    labels = {
      'body': ''
    }