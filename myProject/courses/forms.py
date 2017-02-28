from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions,InlineRadios, Div
from accounts.models import Instructor
import collections

class AttendanceForm(forms.Form):
    enrollment_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    date = forms.DateField(
        widget=forms.TextInput(),
        required=True
    )

    status = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

class ScoreForm(forms.Form):
    enrollment_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    assessment_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    point = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

class CourseForm(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super(CourseForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    def get_department_choices():
        choices_list = (
            ('Computer', 'Computer'),
            ('Civil', 'Civil'),
            ('Electrical', 'Electrical'),
        )

        return choices_list
    
    name = forms.CharField(
        label="Course name",
        widget=forms.TextInput(),
        required=True
    )

    course_number = forms.CharField(
        label="Course number",
        widget=forms.TextInput(),
        required=True
    )

    year = forms.CharField(
        label="Year",
        widget=forms.TextInput(),
        required=True
    )

    semester = forms.ChoiceField(
        choices=(('1',"1"),('2',"2"),('3',"summer")),
        label="Semester",
        widget=forms.RadioSelect,
        required=True

    )

    description = forms.CharField(
        label="Description",
        widget=forms.TextInput(),
        required=True
    )

    major = forms.ChoiceField(
        choices=get_department_choices(),
        label="Department",
        widget=forms.Select(),
        required=True
    )

    section_number = forms.CharField(
        label="Section number",
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
            Field('name', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('course_number', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('year', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            InlineRadios('semester'),css_class='row rearrange-content'
            ),
         Div(
            Field('description', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('major', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )


        # FormActions(Submit('save', 'Save changes'), Button('cancel',('Cancel'))),
        # ButtonHolder(
        #         # Submit('submit', 'Submit'),
        #         Submit('cancel', 'Cancel'),

        #     )
    )


class EditCourseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')

        super(EditCourseForm,self).__init__( *args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'value':self.obj.name})
        self.fields['course_number'].widget = forms.TextInput(attrs={'value':self.obj.course_number})
        self.fields['year'].widget = forms.TextInput(attrs={'value':self.obj.year})
        self.fields['semester'].widget = forms.RadioSelect()
        self.fields['semester'].initial = self.obj.semester
        self.fields['description'].widget = forms.TextInput(attrs={'value':self.obj.description})
        self.fields['major'].widgets = forms.Select()
        self.fields['major'].initial = self.obj.major

    def get_department_choices():
        choices_list = (
            ('Computer', 'Computer'),
            ('Civil', 'Civil'),
            ('Electrical', 'Electrical'),
        )

        return choices_list

    name = forms.CharField(
        label="Course name",
        # widget=forms.TextInput(),
        required=True
    )

    course_number = forms.CharField(
        label="Course number",
        # widget=forms.TextInput(attrs={'value':self.obj.course_number}),
        required=True
    )

    year = forms.CharField(
        label="Year",
        # widget=forms.TextInput(attrs={'value':self.obj.year}),
        required=True
    )

    semester = forms.ChoiceField(
        choices=(('1',"1"),('2',"2"),('3',"summer")),
        label="Semester",
        # widget=forms.RadioSelect,
        required=True

    )

    description = forms.CharField(
        label="Description",
        # widget=forms.TextInput(attrs={'value':self.obj.description}),
        required=True
    )

    major = forms.ChoiceField(
        # choices = get_department_choices(),
        choices=(('Computer', 'Computer'),('Civil', 'Civil'),('Electrical', 'Electrical')),
        label="Department",
        # widget=forms.Select(),
    )
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Div(
            Field('name', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            Field('course_number', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            Field('year', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            InlineRadios('semester'),css_class='row rearrange-content'
            ),
         Div(
            Field('description', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            Field('major', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )
    )



class SectionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')

        super(SectionForm,self).__init__( *args, **kwargs)
        self.fields['name'].widget = forms.TextInput(attrs={'value':self.obj.name})
        self.fields['course_number'].widget = forms.TextInput(attrs={'value':self.obj.course_number})
        self.fields['year'].widget = forms.TextInput(attrs={'value':self.obj.year})
        self.fields['semester'].widget = forms.RadioSelect()
        self.fields['semester'].initial = self.obj.semester
        self.fields['description'].widget = forms.TextInput(attrs={'value':self.obj.description})
        self.fields['major'].widgets = forms.Select()
        self.fields['major'].initial = self.obj.major

    def get_instructor_choices():
        instructor_list = Instructor.objects.all()
        choices_list = {'----Select Instructor----':'----Select Instructor----'}
        for instructor in instructor_list:
            choices_list[instructor.instructor_id] = instructor.first_name +" "+ instructor.last_name

        return ((k,v) for k,v in choices_list.items())

    name = forms.CharField(
        label="Course name",
        required=True
    )

    course_number = forms.CharField(
        label="Course number",
        required=True
    )

    year = forms.CharField(
        label="Year",
        required=True
    )

    semester = forms.ChoiceField(
        choices=(('1',"1"),('2',"2"),('3',"summer")),
        label="Semester",
        required=True

    )

    description = forms.CharField(
        label="Description",
        required=True
    )

    major = forms.ChoiceField(
        choices=(('Computer', 'Computer'),('Civil', 'Civil'),('Electrical', 'Electrical')),
        label="Department",
        required=True
    )  

    #section infomation
    section_number = forms.CharField(
        # label="Section number",
        widget=forms.TextInput(),
        required=True
    )

    time = forms.CharField(
        # label="Time",
        widget=forms.TextInput(),
        required=True
    )

    instructor_id = forms.ChoiceField(
        # queryset=Instructor.objects.all()
        choices=get_instructor_choices(),
        label="Instructor",
        widget=forms.Select(),
        required=True
    )

    # grade_criteria = forms.CharField(
    #     widget=forms.Textarea(),
    #     required=True
    # )

    # year = forms.CharField(
    #     widget=forms.TextInput(),
    #     required=True
    # )

    # semester = forms.CharField(
    #     widget=forms.TextInput(),
    #     required=True
    # )

    # course_number = forms.CharField(
    #     widget=forms.TextInput(),
    #     required=True
    # )


    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Div(
            Field('name', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
        Div(
            Field('course_number', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
        Div(
            Field('section_number', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
        Div(
            Field('time', css_class='input-sm re-color '),css_class='row rearrange-content'
            ),
        Div(
            Field('instructor_id', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
        # Div(
        #     Field('grade_criteria', css_class='input-sm re-color expand-text-area'),css_class='row rearrange-content'
        #     ),
        Div(
            Field('year', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
        Div(
            InlineRadios('semester'),css_class='row rearrange-content'
            ),
        Div(
            Field('description', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
        Div(
            Field('major', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
            ),
        
        Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )
    )


class AssessmentForm(forms.Form):
    max_point = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    weight = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    date = forms.DateField(
        widget=forms.TextInput(),
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-6'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Div(
            Field('max_point', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
        Div(
            Field('weight', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
        Div(
            Field('date', css_class='input-sm re-color'),css_class='row rearrange-content'
            ),
         Div(
            ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
            )
    )


class EnrollmentForm(forms.Form):
    student_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    section_number = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    grade = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

class GradeCriteriaForm(forms.Form):
    grade_criteria = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    range_start = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    range_end = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    grade = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )
