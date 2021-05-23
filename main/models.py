from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class importantPDF(models.Model):
    title = models.CharField(max_length=100)
    pdf_file = models.FileField(upload_to='files/',
                                validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    timeAdded=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
