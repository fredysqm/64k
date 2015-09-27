from django import forms
from app.models import slink

from django.core import validators
from django.template import defaultfilters

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button
from crispy_forms.bootstrap import FormActions


class slink_crear_form(forms.ModelForm):
    use_custom_slug = forms.BooleanField(label="Personalizar", required=False)
    custom_slug = forms.CharField(label="http://64k.in/", max_length=16, required=False, validators=[validators.MaxLengthValidator(16)])

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-md-2'
    helper.field_class = 'col-md-10'
    helper.layout = Layout(
        'url',
        'use_custom_slug',
        'custom_slug',
        FormActions(
            Submit('submit', 'Cortar URL'),
            css_class='text-right'
        ),
    )

    class Meta:
        model = slink
        fields = ('url',)