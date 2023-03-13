from django.db import models

# Create your models here.
class Memo(models.Model):
    memo_text = models.CharField(max_length=250)
    published_date = models.DateField(auto_now_add=True)