from django import forms
TEMPLATE_CHOICES= [
    ('basic', 'Basic'),
    ('rhombus', 'Rhombus'),
    ('snap', 'Snap'),
    ('vienna', 'Vienna'),
    ('summer','Summer')
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
    ('other','Other'),
]
class Form(forms.Form):
    url=forms.URLField()
    template = forms.CharField(label='Video Template', widget=forms.Select(choices=TEMPLATE_CHOICES))
    currency = forms.CharField(label='Currency Unit', widget=forms.Select(choices=CURR_CHOICES,attrs={'onchange':"return validateForm();"}))
    # Other = forms.CharField(max_length=30, required = False, widget = forms.TextInput(attrs={'style':"display: none;"}))
