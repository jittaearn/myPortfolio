from django import forms
from portfolio.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'subject': forms.Textarea(
                attrs={
                    'id': 'subject',
                    'style' : 'height: 40px; font-size: 18px; resize: none; display: inline;',
                    'class' : 'col-12 mt-2 p-2 d-flex justify-content-center',
                }
            ),
            'email':forms.Textarea(
                attrs={
                    'id': 'email',
                    'style' : 'height: 40px; font-size: 18px; resize: none; display: inline;',
                    'class' : 'col-12 mt-2 p-2 d-flex justify-content-center',
                }
            ),
            'comment':forms.Textarea(
                attrs={
                    'id': 'comment',
                    'style' : 'height: 250px; font-size: 18px; border-radius: 1rem;',
                    'class' : 'col-12 mt-2 p-3 d-flex justify-content-center',
                }
            )
        }