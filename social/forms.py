from django import forms
from .models import SocialPost, SocialComment


class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-rose-400 focus:border-rose-400 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-rose-500 rounded-md',
            'rows': '5',
            'placeholder': 'Comparti lo que queras..'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium    hover:text-rose-500  focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-rose-400 form-label inline-block mb-2 text-gray-700',
        'multiple': True
        }),
        required=False
        )

    class Meta:
        model=SocialPost
        fields=['body']


class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '5',
            'placeholder': 'Comment Something...'
            }),
        required=True
        )
        




    class Meta:
        model=SocialComment
        fields=['comment']



class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-rose-400 focus:border-rose-400 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-rose-500 rounded-md',
            'rows': '5',
            'placeholder': 'Say Something...'
            }),
        )


