from django import forms
from django.contrib.auth.models import User 
from .models import Profile 



class UserRegistrationForm(forms.ModelForm): 
    password  =  forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 =  forms.CharField(label =  'Repeat password', widget = forms.PasswordInput)

    class Meta: 
        model = User
        fields  = ['email']

    """Hàm kiểm tra """
    def clean_password2(self): 
        cd = self.cleaned_data

        if cd['password'] != cd['password2'] : raise forms.ValidationError('Password don\' match')

        return cd['password2']
    
    '''Hàm kiểm tra email đã tồn tại hay chưa'''
    def clean_email(self): 
        cd = self.cleaned_data

        if User.objects.filter(email = cd['email']).exists() : 
            raise forms.ValidationError("Email already use.")

        return cd['email']
    

class UserEditForm(forms.ModelForm): 

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email']


    def clean_email(self): 
        data = self.cleaned_data['email']

        if User.objects.exclude(id = self.instance.id).filter(email = data).exists() : 
            raise forms.ValidationError("Email already in use")
        
        return data 

class ProfileForm(forms.ModelForm) : 
    class Meta: 
        model = Profile
        fields = ['date_of_birth', 'user', 'phone', 'address']






    




