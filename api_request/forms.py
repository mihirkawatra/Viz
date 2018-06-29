from django import forms
TEMPLATE_CHOICES= [
    ('basic', 'Basic'),
    ('rhombus', 'Rhombus'),
    #('', ''),
    ]
CURR_CHOICES = [
    ('$','United States dollar ($)'),
    ('€','Euro (€)'),
    ('¥','Japanese Yen (¥)'),
    ('£','Pound Sterling (£)'),
    ('$','Australian Dollar ($)'),
    ('Fr','Swiss Franc (Fr)'),
    ('$','Canadian Dollar ($)'),
    ('$','Hong Kong Dollar ($)'),
    ('kr','Swedish Kronor (kr)'),
]
class Form(forms.Form):
    url=forms.URLField()
    template = forms.CharField(label='Video Template: ', widget=forms.Select(choices=TEMPLATE_CHOICES))
    currency = forms.CharField(label='Currency Unit: ', widget=forms.Select(choices=CURR_CHOICES))
