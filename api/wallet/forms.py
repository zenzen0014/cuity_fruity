from django import forms
from wallet.models import Category, Person

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'category', 'proximity', 'email',)