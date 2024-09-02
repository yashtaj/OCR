from django.db import models

class ExtractedText(models.Model):
    image = models.ImageField(upload_to='images/')
    text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Text from {self.image.name} uploaded at {self.uploaded_at}"
