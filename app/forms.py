from django import forms
from app.models import slink

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout,  Button
from crispy_forms.bootstrap import FormActions


class slink_crear_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(slink_crear_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-10'

        self.helper.layout = Layout(
            'url',
            FormActions(
                Submit('submit', 'Cortar URL'),
                css_class='text-right'
            ),
        )

    class Meta:
        model = slink
        fields = ('url',)