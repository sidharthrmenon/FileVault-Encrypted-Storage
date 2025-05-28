from django.db import models


# Create your models here.
class UserLogin(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=300)
    user_image = models.ImageField(upload_to='user_images/')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    feedback = models.TextField(default='')
    rating = models.IntegerField(default=1)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Feedback from {self.user.username} - {self.created_at}"


class UploadedFile(models.Model):
    user = models.ForeignKey(UserLogin, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    file_type = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name


class DownloadRequest(models.Model):
    file = models.ForeignKey(UploadedFile, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(UserLogin, on_delete=models.CASCADE, related_name='requests_made')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved')],
                              default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requested_by.username} → {self.file.file.name} ({self.status})"
