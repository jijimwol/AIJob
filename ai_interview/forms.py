from django import forms
from .models import InterviewPractice

class QuestionForm(forms.Form):
    domain = forms.ChoiceField(choices=[
        ('Software Engineer', 'Software Engineer'),
        ('Data Scientist', 'Data Scientist'),
        ('Marketing', 'Marketing'),
        ('Product Manager', 'Product Manager'),
        ('Cybersecurity Analyst', 'Cybersecurity Analyst'),
        ('Cloud Engineer', 'Cloud Engineer'),
        ('DevOps Engineer', 'DevOps Engineer'),
        ('AI/ML Engineer', 'AI/ML Engineer'),
        ('Business Analyst', 'Business Analyst'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Project Manager', 'Project Manager'),
        ('Quality Assurance Engineer', 'Quality Assurance Engineer'),
        ('Human Resources', 'Human Resources'),
        ('Finance Analyst', 'Finance Analyst'),
        ('Sales Representative', 'Sales Representative'),
    ], label="Select Domain")

    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter job details...'}),
        label="Job Description"
    )

class AnswerForm(forms.ModelForm):
    class Meta:
        model = InterviewPractice
        fields = ['user_answer']
        widgets = {
            'user_answer': forms.Textarea(attrs={'placeholder': 'Type your answer here...'})
        }
