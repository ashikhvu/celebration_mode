from django.db import models

class EventModel(models.Model):
    event_name = models.CharField(max_length=255)
    def __str__(self):
        return self.event_name

class ThemesModel(models.Model):
    theme_name = models.ForeignKey(EventModel,on_delete=models.CASCADE,null=True)
