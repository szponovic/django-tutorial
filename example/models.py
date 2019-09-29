from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    relased = models.CharField(max_length=128)
    created_on = models.DateTimeField(auto_now_add=True)
    #rating = models.FloatField(default=0)
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    about = models.CharField(max_length=1280, default="")
    viewed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
# Create your models here.
