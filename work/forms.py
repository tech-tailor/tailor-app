from django import forms



class WorkerForm(forms.Form):
    first_name = forms.CharField(
        label = 'first name',
        widget=forms.TextInput(attrs={'placeholder': 'First name'}),
    )
    last_name = forms.CharField(
        label = 'last name',
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}),
    )
    #Phone_Number = forms.CharField(
    #    label = 'Phone Number',
     #   widget=forms.TextInput(attrs={'placeholder': 'Top Lenght'}),
    #)
    
    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}))
    
    
  