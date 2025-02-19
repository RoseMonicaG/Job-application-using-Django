from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'phone_number', 'resume', 'cover_letter']
    
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            if not resume.name.endswith('.pdf'):
                raise forms.ValidationError('Only PDF files are allowed.')
        return resume
