from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder, HTML, Hidden
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions,InlineRadios, Div
from django.contrib.auth.models import User,Group

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
    email = forms.EmailField(
        label='Email Address',
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
            Field('email', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('department', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )

    )


class InstructorProfileForm(forms.Form):
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

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')

        super(InstructorProfileForm,self).__init__( *args, **kwargs)
        user_info = User.objects.get(username=self.obj.instructor_id)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-6'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            # Div(
            #     HTML(
            #         '<label class="control-label col-sm-16 change-header-color">'+
            #             'Your Profile'
            #         ),css_class='row rearrange-content'
            #     ), 
            Div(
                HTML(
                    '<label for="id_degree" class="control-label col-sm-6 ">'+
                        'Degree'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.degree+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_first_name" class="control-label col-sm-6 ">'+
                        'First name'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.first_name+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_last_name" class="control-label col-sm-6 ">'+
                        'Last name'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.last_name+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_instructor_id" class="control-label col-sm-6 ">'+
                        'Instructor ID'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+str(self.obj.instructor_id)+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_email" class="control-label col-sm-6 ">'+
                        'Email address'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+user_info.email+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_department" class="control-label col-sm-6 ">'+
                        'Department'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.department+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                Hidden('instructor_id', self.obj.instructor_id)
                ),
        )

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
    email = forms.EmailField(
        label='Email Address',
        required=True
    )
    department = forms.ChoiceField(
        choices=get_department_choices(),
        label="Department",
        widget=forms.Select(),
        required=True
    )
    instructor_picture = forms.CharField(
        label="Picture",
        widget=forms.TextInput(),
    )



class EditInstructorProfileForm(forms.Form):
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

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')

        super(EditInstructorProfileForm,self).__init__( *args, **kwargs)
        user_info = User.objects.get(username=self.obj.instructor_id)
        self.fields['degree'].widgets = forms.Select()
        self.fields['degree'].initial = self.obj.degree
        self.fields['first_name'].widget = forms.TextInput(attrs={'value':self.obj.first_name})
        self.fields['last_name'].widget = forms.TextInput(attrs={'value':self.obj.last_name})
        self.fields['email'].widget = forms.TextInput(attrs={'value':user_info.email})
        self.fields['department'].widgets = forms.Select()
        self.fields['department'].initial = self.obj.department
        self.fields['instructor_picture'].widget = forms.TextInput(attrs={'value':self.obj.instructor_picture})

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-6'
        self.helper.field_class = 'col-sm-4'
        self.helper.layout = Layout(
            Div(
                Field('degree', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                Field('first_name', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                Field('last_name', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                HTML(
                    '<label for="id_instructor_id" class="control-label col-sm-6 ">'+
                        'Instructor ID'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+str(self.obj.instructor_id)+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                Field('email', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                Field('department', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                Field('instructor_picture', css_class='input-sm re-color'),css_class='row rearrange-content'
                ),
            Div(
                Hidden('instructor_id', self.obj.instructor_id)
                ),
            Div(
                ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )
        )

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
    email = forms.EmailField(
        label='Email Address',
        required=True
    )
    department = forms.ChoiceField(
        choices=get_department_choices(),
        label="Department",
        widget=forms.Select(),
        required=True
    )
    instructor_picture = forms.CharField(
        label="Picture",
        widget=forms.TextInput(),
    )

