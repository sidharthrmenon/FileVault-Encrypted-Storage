from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(UserLogin)
admin.site.register(Feedback)
admin.site.register(UploadedFile)
admin.site.register(DownloadRequest)
