from django.db import models
from django.core.validators import RegexValidator

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^[0-9]{10}$', message='Phone number must be 10 digits.')]
    )
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


