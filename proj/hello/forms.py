from django import forms

class ContactForm(forms.Form):

    message = forms.CharField(
        #max_length=2000,
        widget=forms.Textarea()
    )
 

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        message = cleaned_data.get('message')