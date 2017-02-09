from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import PrependedText, PrependedAppendedText, FormActions,InlineRadios


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
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

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

    major = forms.CharField(
        label="Major",
        widget=forms.TextInput(),
        required=True
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('name', css_class='input-sm'),
        Field('course_number', css_class='input-sm'),
        Field('year', css_class='input-sm'),
        InlineRadios('semester'),
        #Field('semester', css_class='input-sm'),
        Field('description', rows=3),
        Field('major', css_class='input-sm'),
        FormActions(Submit('course', 'course', css_class='btn-primary'))
    )

class AssessmentForm(forms.Form):
    section_number = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    assessment_type = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

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
        required=True
    )

class SectionForm(forms.Form):
    course_number = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    section_number = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    year = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    semester = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    grade_criteria = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    time = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    instructor_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
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
