from django import forms
from app.models import slink

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Button, Fieldset
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions


class slink_crear_form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(slink_crear_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-9'

        self.helper.layout = Layout(
            Fieldset(u'<span class="glyphicon glyphicon-scissors"></span> Cortar URL',
                'url',
                FormActions(
                    Submit('submit', u'Cortar'),
                    css_class='text-right'
                ),
            ),

        )

    class Meta:
        model = slink
        fields = ('url',)