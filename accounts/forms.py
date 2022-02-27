from accounts.models import Profile
from django import forms



class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out',
            })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out',
            })
    )
    picture = forms.ImageField(label='Profile Picture',required=False, widget=forms.FileInput)
    banner = forms.ImageField(label='Banner Picture',required=False, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), max_length=60, required=False)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), max_length=260, required=False)
    birthday = forms.DateField(widget= forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), required=False)

    class Meta:
        model = Profile
        fields = ('first_name','last_name','picture','banner','location','url','bio','birthday')