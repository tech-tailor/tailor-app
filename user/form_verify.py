from django import forms


class VerificationForm(forms.Form):
      verification_code = forms.CharField(
        label='Verification Code',
        widget=forms.TextInput(attrs={'placeholder': 'Enter verification code'}),
        max_length=6,
        required=True,
    )