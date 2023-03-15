from django import forms
from .models import BlogPost
from .models import Application
from .models import Staff
from .models import DocumentFile
# from django.contrib.auth.models import User
from .models import User
from .models import Document
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class UploadFileForm(forms.Form):
    file = forms.FileField()

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('applicant_name', 'item', 'quantity', 'reason')

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

class ApprovalRequestForm(forms.Form):
    document_type = forms.ChoiceField(choices=[(1, 'Purchase Order'), (2, 'Travel Request'), (3, 'Expense Report')], required=True)
    document_number = forms.CharField(max_length=100, required=True)
    approver = forms.CharField(max_length=100, required=True)
    comments = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)
        
class UserForm(forms.ModelForm):
    class Meta:
        model= Staff
        fields=['address','mobile','profile_pic']

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_name', 'uploaded_by', 'uploaded_date', 'document_file','approved']
        exclude = ('approved',)
        widgets = {
            'document_name': forms.TextInput(attrs={'class': 'form-control'}),
            'uploaded_by': forms.TextInput(attrs={'class': 'form-control'}),
            'uploaded_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'document_file': forms.FileInput(attrs={'class': 'form-control-file'})
        }



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))