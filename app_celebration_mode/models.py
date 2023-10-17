from django.db import models

class ThemesModel(models.Model):
    theme_name = models.CharField(max_length=255)
