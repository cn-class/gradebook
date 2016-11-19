from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )

    student_id = forms.IntegerField(
        widget=forms.TextInput(),
        required=True
    )

    major = forms.CharField(
        widget=forms.TextInput(),
        required=True
    )
