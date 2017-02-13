from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions,InlineRadios, Div

class StudentForm(forms.Form):
    def get_department_choices():
        choices_list = (
            ('Computer', 'Computer'),
            ('Civil', 'Civil'),
            ('Electrical', 'Electrical'),
        )

        return choices_list

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(),
        required=True
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(),
        required=True
    )

    student_id = forms.IntegerField(
        label="Student ID",
        widget=forms.TextInput(),
        required=True
    )

    major = forms.ChoiceField(
        choices=get_department_choices(),
        label="Major",
        widget=forms.Select(),
        required=True
    )
    student_picture = forms.CharField(
        label="Student picture",
        widget=forms.TextInput(),
        required=True
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
         Div(
            Field('first_name', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('last_name', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         
         Div(
            Field('student_id', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('major', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            Field('student_picture', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )

    )

class InstructorForm(forms.Form):

    def get_degree_choices():
        choices_list = (
            ('Bachelor', 'Bachelor Degree'),
            ('Master', 'Masters Degree'),
            ('Doctoral', 'Doctoral Degree'),
        )

        return choices_list

    def get_department_choices():
        choices_list = (
            ('Computer', 'Computer'),
            ('Civil', 'Civil'),
            ('Electrical', 'Electrical'),
        )

        return choices_list

    degree = forms.ChoiceField(
        choices=get_degree_choices(),
        label="Degree",
        widget=forms.Select(),
        required=True
    )

    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(),
        required=True
    )

    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(),
        required=True
    )

    instructor_id = forms.IntegerField(
        label="Instructor ID",
        widget=forms.TextInput(),
        required=True
    )

    department = forms.ChoiceField(
        choices=get_department_choices(),
        label="Department",
        widget=forms.Select(),
        required=True
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Div(
            Field('degree', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            Field('first_name', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('last_name', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         
         Div(
            Field('instructor_id', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('department', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )

    )