# ============================
# 📘 DJANGO FORMS FIELD CHEAT SHEET
# Paste this directly in your forms.py for easy reference
# ============================

# 🧩 COMMON FIELD OPTIONS (shared across most field types)
# -------------------------------------------------------
# label            : str - Display name of the field
# required         : bool - Whether field is mandatory (default=True)
# initial          : any - Initial/default value
# help_text        : str - Text shown next to the form field
# disabled         : bool - If True, field is displayed but not editable
# widget           : Widget instance - HTML representation
# error_messages   : dict - Customize validation errors (e.g. {'required': 'This field is needed'})
# validators       : list - Custom validation functions
# localize         : bool - Apply localization formatting
# label_suffix     : str - Character to show after label (e.g., ":")

# ============================
# 🔤 CharField (Text input)
# ============================
# max_length       : int - Max allowed characters
# min_length       : int - Min required characters
# strip            : bool - Trim whitespace from both ends (default=True)

# Example:
# forms.CharField(
#     max_length=100,
#     min_length=3,
#     label='Username',
#     help_text='Enter your unique username',
#     required=True
# )

# ============================
# 🔢 IntegerField, FloatField, DecimalField
# ============================
# min_value        : int/float/decimal - Minimum value allowed
# max_value        : int/float/decimal - Maximum value allowed
# decimal_places   : int - For DecimalField, number of digits after decimal
# max_digits       : int - For DecimalField, total number of digits

# Example:
# forms.IntegerField(
#     min_value=18,
#     max_value=100,
#     label='Your Age',
#     help_text='Must be between 18 and 100'
# )

# ============================
# 📧 EmailField (with built-in email validation)
# ============================
# max_length       : int - Max length of the email address

# Example:
# forms.EmailField(
#     max_length=254,
#     help_text='Enter a valid email address',
#     required=True
# )

# ============================
# 🌐 URLField
# ============================
# Example:
# forms.URLField(
#     required=False,
#     label='Your website'
# )

# ============================
# ✅ BooleanField (checkbox input)
# ============================
# required         : True means checkbox must be ticked
# Example:
# forms.BooleanField(
#     required=True,
#     label='I agree to terms and conditions'
# )

# ============================
# 📅 DateField / TimeField / DateTimeField
# ============================
# input_formats    : list of accepted input string formats
# widget           : DateInput/TimeInput/DateTimeInput

# Example:
# forms.DateField(
#     widget=forms.DateInput(attrs={'type': 'date'}),
#     input_formats=['%Y-%m-%d'],
#     required=False
# )

# ============================
# 📂 FileField / ImageField (uploading files)
# ============================
# FileField → accepts any file
# ImageField → requires Pillow, validates image formats
# required=False → allows empty file input

# Example:
# forms.ImageField(
#     required=False,
#     label='Upload a profile picture'
# )

# ============================
# 🔘 ChoiceField / MultipleChoiceField
# ============================
# choices          : tuple/list of (value, label)
# widget           : Dropdown by default, can be RadioSelect, CheckboxSelectMultiple, etc.

# Example:
# forms.ChoiceField(
#     choices=[('M', 'Male'), ('F', 'Female')],
#     label='Gender'
# )

# forms.MultipleChoiceField(
#     choices=[('R', 'Reading'), ('C', 'Coding')],
#     widget=forms.CheckboxSelectMultiple,
#     label='Hobbies'
# )

# ============================
# 🔄 ModelChoiceField / ModelMultipleChoiceField
# ============================
# queryset         : queryset of model instances
# empty_label      : str - Label for empty choice (ModelChoiceField only)
# to_field_name    : str - Field used to determine the value (default is 'pk')

# Example:
# forms.ModelChoiceField(
#     queryset=User.objects.all(),
#     empty_label="Select a user",
#     to_field_name='username'
# )

# forms.ModelMultipleChoiceField(
#     queryset=Tag.objects.all(),
#     widget=forms.CheckboxSelectMultiple
# )

# ============================
# ✍️ Customizing widgets
# ============================
# Add CSS classes, placeholders, and HTML attributes:
# Example:
# forms.CharField(
#     widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'placeholder': 'Enter your name'
#     })
# )

# ============================
# 📢 Custom error messages
# ============================
# forms.CharField(
#     error_messages={
#         'required': 'This field cannot be empty!',
#         'max_length': 'Too many characters!'
#     }
# )

# ============================
# 🛠 Custom validators
# ============================
# from django.core.exceptions import ValidationError
# def must_start_with_r(value):
#     if not value.lower().startswith('r'):
#         raise ValidationError('Value must start with "r".')

# forms.CharField(validators=[must_start_with_r])

# ============================
# 🧙 Example Full Field
# ============================
# caption = forms.CharField(
#     max_length=200,
#     min_length=2,
#     required=True,
#     label="Post Caption",
#     help_text="Write something cool!",
#     widget=forms.Textarea(attrs={
#         'rows': 4,
#         'placeholder': 'Say something...',
#         'class': 'form-control'
#     }),
#     error_messages={
#         'required': 'You can’t post an empty thought!',
#         'max_length': 'Caption too long. Shorten it!'
#     }
# )


###########################################################################################

# ─── DJANGO FORM FIELD ➜ WIDGET CHEAT SHEET ───────────────────────────────────

# CharField ➜ TextInput
# forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter text'}))

# CharField ➜ Textarea (for long text)
# forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write more...'}))

# EmailField ➜ EmailInput
# forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'you@example.com'}))

# URLField ➜ URLInput
# forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'https://your.site'}))

# IntegerField / FloatField ➜ NumberInput
# forms.IntegerField(widget=forms.NumberInput(attrs={'min': 0, 'max': 100}))
# forms.FloatField(widget=forms.NumberInput(attrs={'step': 0.01}))

# DecimalField ➜ NumberInput
# forms.DecimalField(widget=forms.NumberInput(attrs={'step': '0.01'}))

# DateField ➜ DateInput
# forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

# DateTimeField ➜ DateTimeInput
# forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

# BooleanField ➜ CheckboxInput
# forms.BooleanField(widget=forms.CheckboxInput())

# ChoiceField ➜ Select
# forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

# ChoiceField ➜ RadioSelect
# forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

# MultipleChoiceField ➜ SelectMultiple
# forms.MultipleChoiceField(choices=CHOICES, widget=forms.SelectMultiple())

# ModelChoiceField ➜ Select
# forms.ModelChoiceField(queryset=Model.objects.all(), widget=forms.Select())

# ModelMultipleChoiceField ➜ SelectMultiple
# forms.ModelMultipleChoiceField(queryset=Model.objects.all(), widget=forms.SelectMultiple())

# FileField / ImageField ➜ FileInput or ClearableFileInput
# forms.FileField(widget=forms.FileInput(attrs={'accept': 'image/*'}))
# forms.ImageField(widget=forms.ClearableFileInput())

# Password (CharField) ➜ PasswordInput
# forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))

# HiddenField (e.g. CharField) ➜ HiddenInput
# forms.CharField(widget=forms.HiddenInput())

# NullBooleanField ➜ NullBooleanSelect
# forms.NullBooleanField(widget=forms.NullBooleanSelect())

# ─────────────────────────────────────────────────────────────────────────────

# Example of applying widgets inside Meta:
# class Meta:
#     model = YourModel
#     fields = ['title', 'caption']
#     widgets = {
#         'title': forms.TextInput(attrs={'placeholder': 'Enter your post title'}),
#         'caption': forms.Textarea(attrs={'rows': 5}),
#     }

# You can override any field like this too:
# title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

# ─────────────────────────────────────────────────────────────────────────────


##################################################################################################


# ─── DJANGO FORM META OPTIONS CHEAT SHEET ─────────────────────────────────────

# 'model': The model class this form is tied to (Required)
# class Meta:
#     model = YourModel  # The model you're creating the form for

# 'fields': A list or tuple of field names you want to include in the form
# class Meta:
#     fields = ['title', 'caption', 'image']  # Only include these fields

# 'exclude': A list/tuple of field names you want to exclude (mutually exclusive with 'fields')
# class Meta:
#     exclude = ['created_at', 'updated_at']  # Include everything except these

# 'labels': Custom labels for fields (replaces default verbose_name)
# class Meta:
#     labels = {
#         'title': 'Post Title',
#         'caption': 'What’s on your mind?',
#     }

# 'help_texts': Helper text shown under form inputs
# class Meta:
#     help_texts = {
#         'title': 'Keep it short and sweet',
#         'image': 'JPEG or PNG format only',
#     }

# 'widgets': Customize how a field renders (form control type and its attributes)
# class Meta:
#     widgets = {
#         'title': forms.TextInput(attrs={'placeholder': 'Your title here...'}),
#         'caption': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write something...'}),
#         'is_archived': forms.CheckboxInput(),
#         'date_published': forms.DateInput(attrs={'type': 'date'}),
#     }

# ─────────────────────────────────────────────────────────────────────────────

# 🔥 Pro Tip:
# You can combine all of these in one Meta:
#
# class Meta:
#     model = Post
#     fields = ['title', 'caption', 'image', 'is_archived']
#     labels = {
#         'title': 'Post Title',
#     }
#     help_texts = {
#         'caption': 'Say something thoughtful...',
#     }
#     widgets = {
#         'caption': forms.Textarea(attrs={'rows': 3}),
#         'is_archived': forms.CheckboxInput(),
#     }

# ─────────────────────────────────────────────────────────────────────────────



from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'caption',
            'media',
            'visibility'
            # Song ,
            #  location,
            ]

        labels = {
            'title': 'Title:',
            'caption': 'Caption:',
            'media': 'Upload a file:',
            'visibility': 'Show this post to:'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Enter the title"
            }),
            'caption': forms.Textarea(attrs={
                'rows': '10',
                'cols': "50",
                'placeholder': 'Enter the caption',
            }),
            'media': forms.ClearableFileInput(),
            'visibility': forms.Select()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''