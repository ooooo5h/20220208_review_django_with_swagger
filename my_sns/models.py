from django.db import models

# Create your models here.
class FeedImages(models.Model):
    feed = models.ForeignKey('Feeds', models.DO_NOTHING, blank=True, null=True)
    img_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'feed_images'


class FeedReplies(models.Model):
    feed = models.ForeignKey('Feeds', models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_replies'


class Feeds(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    lecture = models.ForeignKey('Lectures', models.DO_NOTHING, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feeds'


class LectureUser(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    lecture = models.ForeignKey('Lectures', models.DO_NOTHING)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture_user'


class Lectures(models.Model):
    title = models.CharField(max_length=20)
    campus = models.CharField(max_length=10)
    fee = models.IntegerField()
    teacher = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectures'


class User(models.Model):
    email = models.CharField(max_length=50)
    password_hashed = models.CharField(max_length=32)
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_year = models.IntegerField()
    is_male = models.IntegerField()
    is_admin = models.IntegerField()
    home_latitude = models.FloatField(blank=True, null=True)
    home_longitude = models.FloatField(blank=True, null=True)
    profile_img_url = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField()
    retired_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'