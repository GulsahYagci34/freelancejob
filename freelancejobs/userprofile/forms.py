from django import forms


class LoginForm(forms.Form):
     username = forms.CharField(label = "Kullanıcı Adı")
     password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    email = forms.CharField(max_length=254)
    username = forms.CharField(max_length = 50,label = "Kullanıcı Adı")
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if  password != confirm:
            raise forms.ValidationError("Parola Eşleşmiyor")
        
        values = {
             "username" : username,
            "email" : email,
            "password" : password 
        }
        
        return values