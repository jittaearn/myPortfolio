from django.db import models
from django.utils import timezone

class Comment(models.Model):
    comment_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.comment_txt
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Email(models.Model):
    comment_txt = models.ForeignKey(Comment, on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.email