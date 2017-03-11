from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Fieldset, ButtonHolder,HTML, Hidden
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
        # choices = get_department_choices(),
        choices=(('Computer', 'Computer'),('Civil', 'Civil'),('Electrical', 'Electrical')),
        label="Department",
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

class EditSectionForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.obj = kwargs.pop('obj')
        super(EditSectionForm,self).__init__( *args, **kwargs)
        self.fields['section_number'].widget = forms.TextInput(attrs={'value':self.obj.section_number})
        self.fields['year'].widget = forms.TextInput(attrs={'value':self.obj.year})
        self.fields['semester'].widget = forms.RadioSelect()
        self.fields['semester'].initial = self.obj.semester
        self.fields['time'].widget = forms.TextInput(attrs={'value':self.obj.time})
        self.fields['instructor_id'].widgets = forms.Select()
        self.fields['instructor_id'].initial = self.obj.instructor.instructor_id

        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-6'
        self.helper.field_class = 'col-sm-4'
        course_number = self.obj.course.course_number
        select_section_number = self.obj.section_number
        self.helper.layout = Layout(
            Div(
                HTML(
                    '<label for="id_course_name" class="control-label col-sm-6 ">'+
                        'Course Name'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.course.name+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_course_number" class="control-label col-sm-6 ">'+
                        'Course Number'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+course_number+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                Field('section_number', css_class='input-sm re-color'),css_class='row rearrange-content'
                ),
            Div(
                InlineRadios('semester'),css_class='row rearrange-content'
                ),
            Div(
                Field('year', css_class='input-sm re-color'),css_class='row rearrange-content'
                ),
            Div(
                Field('time', css_class='input-sm re-color '),css_class='row rearrange-content'
                ),
            Div(
                Field('instructor_id', css_class='input-sm re-color expand-height'),css_class='row rearrange-content'
                ),
            Div(
                HTML(
                    '<label for="id_description" class="control-label col-sm-6 ">'+
                        'Course description'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.course.description+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                HTML(
                    '<label for="id_major" class="control-label col-sm-6 ">'+
                        'Major'+
                    '</label>'+
                    '<div class="controls col-sm-4">'+self.obj.course.major+'</div>'
                    ),css_class='row rearrange-content'
                ), 
            Div(
                Hidden('course_number', self.obj.course.course_number)
                ),
            Div(
                Hidden('select_section_number', select_section_number)
                ),
            Div(
                ButtonHolder(Submit('submit','Submit',css_class="btn btn-info col-sm-4 col-sm-offset-4")),css_class='row rearrange-content'
                )
        )

    def get_department_choices():
        choices_list = (
            ('Computer', 'Computer'),
            ('Civil', 'Civil'),
            ('Electrical', 'Electrical'),
        )

        return choices_list

    def get_instructor_choices():
        instructor_list = Instructor.objects.all()
        choices_list = {'----Select Instructor----':'----Select Instructor----'}
        for instructor in instructor_list:
            choices_list[instructor.instructor_id] = instructor.first_name +" "+ instructor.last_name

        return ((k,v) for k,v in choices_list.items())

    section_number = forms.CharField(
        label="Section number",
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

    time = forms.CharField(
        label="Time",
        required=True
    )

    instructor_id = forms.ChoiceField(
        choices=get_instructor_choices(),
        label="Instructor",
        widget=forms.Select(),
        required=True
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
