from django import forms
from django.core import validators


def check_for_a(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('A... harici giriş yapamaz!')

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    remail = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required = False,
                                 widget = forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    #def clean(self):
    #all_clean_data = super().clean()
    # email = all_clean_data['email']
    # remail=all_clean_data['remail']

    # if email!=remail:
    # raise forms.ValidationError('Eşleşme sağlanamadı!')


    #def clean_botcatcher(self):
       # botcatcher = self.cleaned_data['botcatcher']
      #  if len(botcatcher)>0:
       #     raise  forms.ValidationErrors('GOATCHA BOT')
       # return botcatcher