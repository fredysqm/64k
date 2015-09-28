from django import forms
from app.models import utils, slink

from django.core import validators
from django.template import defaultfilters

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Button
from crispy_forms.bootstrap import FormActions



class slink_crear_form(forms.ModelForm):
    class Meta:
        model = slink
        fields = ('url',)

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

    def clean_custom_slug(self):
        custom_slug = defaultfilters.slugify(self.cleaned_data['custom_slug'])

        if not self.cleaned_data['use_custom_slug']:
            return None

        try:
            slink.objects.get(slug=custom_slug)
            exist_slug = True
        except:
            exist_slug = False

        if exist_slug:
            raise forms.ValidationError('Este nombre ya está en uso.')
        else:
            return custom_slug

    def save(self):
        _slink = super(slink_crear_form, self).save(commit=False)

        if self.cleaned_data['custom_slug'] is None:
            _slink.slug = utils.gen_slug()
        else:
            _slink.slug = self.cleaned_data['custom_slug']

        _slink.save()

        return _slink