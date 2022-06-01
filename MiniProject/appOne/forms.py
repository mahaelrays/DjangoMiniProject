
from django import forms
from django.forms import ModelForm
from appOne.models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content', 'image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
        }

      

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class LoginForm(forms.ModelForm):
		username= forms.CharField(help_text="")
		password = forms.CharField(widget=forms.PasswordInput())
		class Meta:

				model = User

				fields = ('username','password')


class UpdateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields= ['title','author','content', 'image']