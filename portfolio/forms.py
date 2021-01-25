from django import forms
from portfolio.models import Comment

class CommentForm(forms.Form):
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'subject': forms.Textarea(
                attrs={
                    'id': 'subject',
                    'style' : 'height: 50px; font-size: 18px; resize: none',
                    'class' : 'col-10 mt-2 p-3 d-flex justify-content-center',
                }
            ),
            'email':forms.Textarea(
                attrs={
                    'id': 'email',
                    'style' : 'height: 750px; font-size: 18px; border-radius: 3%',
                    'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
                }
            ),
            'comment':forms.Textarea(
                attrs={
                    'id': 'comment',
                    'style' : 'height: 750px; font-size: 18px; border-radius: 3%',
                    'class' : 'col-10 mt-2 p-4 d-flex justify-content-center',
                }
            )
        }