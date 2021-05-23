from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "form-control valid", "name": "email", "id": "email", "type": "email",
                                                           "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter email address'", "placeholder": "Email"}))
    subject = forms.CharField(max_length=254, widget=forms.TextInput(attrs={"class": "form-control", "name": "subject", "id": "subject",
                                                                            "type": "text", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Subject'", "placeholder": "Enter Subject"}))
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control w-100", "name": "message", "id": "message", "cols": "30",
                                                        "rows": "9", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter Message'", "placeholder": " Enter Body"}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"class": "form-control valid", "name": "name", "id": "name",
                                                                         "type": "text", "onfocus": "this.placeholder = ''", "onblur": "this.placeholder = 'Enter your name'", "placeholder": "Enter your name"}))

    def __str__(self):
        return self.Email
