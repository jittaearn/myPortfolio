from django.db import models


class Comment(models.Model):

    subject = models.CharField(max_length= 100)

    email = models.CharField(max_length=100)

    comment = models.TextField( max_length=256)

    def __str__(self):
        return self.comment


