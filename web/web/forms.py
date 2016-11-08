from django import forms

class CreateUser(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    address = forms.CharField(label='Your address', max_length=150)
    cart = forms.CharField(label='Your cart', max_length=100)
    password = forms.CharField(label='Your password', max_length=100)

class CreateShoe(forms.Form):
    shoe = forms.CharField(label='Shoe name', max_length=100)
    brand = forms.CharField(label='Shoe brand', max_length=100)
    text = forms.CharField(label='Shoe description', max_length=300)

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(),label='Password', max_length=100)

# class Search(forms.Form):
#     query = forms.CharField(label='search', max_length=100)
