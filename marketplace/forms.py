from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
   

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out" '}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), required=True)
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), required=True)
    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'
                }), 
            required=True
                )
    
    content_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'block pr-10 shadow appearance-none border-2 border-rose-400 rounded w-full py-2 px-4 text-gray-700 mb-3 leading-tight focus:outline-none focus:bg-white focus:border-rose-400 transition duration-500 ease-in-out'}), required=True)







    class Meta:
        model=Product
        fields=(
            'name',
            'description',
            'thumbnail',
            'slug',
            'content_url',
            'content_file',
            'price',
            'active'
        )

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        price = int(price)
        if price > 99:
            return price
        else:
            raise forms.ValidationError("Price must be equal or higher than $1 == 100")


# class ProductModelForm(forms.ModelForm):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class':'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
#     description = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)
#     slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-r'}), required=True)
#     price = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'
#                 }), 
#             required=True
#                 )
    
#     content_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:focus:ring-dark-second focus:ring-indigo-500 dark:focus:border-dark-second dark:text-dark-txt focus:border-indigo-500 sm:max-w-xs sm:text-sm dark:border-dark-second border-gray-300 rounded-md'}), required=True)

#     class Meta:
#         model=Product
#         fields=(
#             'name',
#             'description',
#             'thumbnail',
#             'slug',
#             'content_url',
#             'content_file',
#             'price',
#             'active'
#         )

#     def clean_price(self, *args, **kwargs):
#         price = self.cleaned_data.get("price")
#         price = int(price)
#         if price > 99:
#             return price
#         else:
#             raise forms.ValidationError("Price must be equal or higher than $1 == 100")