from django import forms


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
    name = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    course_number = forms.CharField(
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

    description = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    major = forms.CharField(
        widget=forms.TextInput(),
        required=True
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
