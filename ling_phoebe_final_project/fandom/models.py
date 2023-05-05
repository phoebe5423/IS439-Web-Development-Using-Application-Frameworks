from django.db import models
from django.db.models import UniqueConstraint
from django.urls import reverse


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.company_name

    class Meta:
        ordering = ['company_name']


class Style(models.Model):
    style_id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.style_name

    def get_absolute_url(self):
        return reverse('fandom_style_detail_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['style_name']


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=45, unique=True)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    company = models.ForeignKey(Company, related_name='group', on_delete=models.PROTECT)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s' % self.group_name
        else:
            result = '%s (%s)' % (self.group_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('fandom_group_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_group_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_group_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['group_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['group_name', 'disambiguator'], name='unique_group')
        ]


class Entertainer(models.Model):
    entertainer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    company = models.ForeignKey(Company, related_name='entertainer', on_delete=models.PROTECT)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s, %s' % (self.last_name, self.first_name)
        else:
            result = '%s, %s (%s)' % (self.last_name, self.first_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('fandom_entertainer_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_entertainer_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_entertainer_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['last_name', 'first_name', 'birth_date', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['last_name', 'first_name', 'birth_date', 'disambiguator'],
                             name='unique_entertainer')
        ]


class EntertainerGroup(models.Model):
    entertainer_group_id = models.AutoField(primary_key=True)
    entertainer = models.ForeignKey(Entertainer, related_name='entertainer_group', on_delete=models.PROTECT)
    group = models.ForeignKey(Group, related_name='entertainer_group', on_delete=models.PROTECT)

    def __str__(self):
        return '%s (%s, %s)' % (self.group.group_name, self.entertainer.last_name, self.entertainer.first_name)

    def get_absolute_url(self):
        return reverse('fandom_entertainergroup_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_entertainergroup_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_entertainergroup_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['entertainer', 'group']
        constraints = [
            UniqueConstraint(fields=['entertainer', 'group'], name='unique_entertainer_group')
        ]


class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=45)
    released_date = models.DateField()
    publisher = models.ForeignKey(Company, related_name='album', on_delete=models.PROTECT)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    style = models.ForeignKey(Style, related_name='album', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s' % self.album_name
        else:
            result = '%s (%s)' % (self.album_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('fandom_album_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_album_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_album_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['album_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['album_name', 'released_date', 'disambiguator'], name='unique_album')
        ]


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=45)
    released_date = models.DateField()
    publisher = models.ForeignKey(Company, related_name='song', on_delete=models.PROTECT, blank=True, null=True)
    album = models.ForeignKey(Album, related_name='song', on_delete=models.PROTECT, blank=True, null=True)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    style = models.ForeignKey(Style, related_name='song', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s' % self.song_name
        else:
            result = '%s (%s)' % (self.song_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('fandom_song_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_song_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_song_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['song_name', 'disambiguator', 'released_date']
        constraints = [UniqueConstraint(fields=['song_name', 'disambiguator', 'album'], name='unique_song')]


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.role_name

    class Meta:
        ordering = ['role_name']


class Create(models.Model):
    create_id = models.AutoField(primary_key=True)
    entertainer = models.ForeignKey(Entertainer, related_name='create', on_delete=models.PROTECT)
    role = models.ForeignKey(Role, related_name='create', on_delete=models.PROTECT)
    song = models.ForeignKey(Song, related_name='create', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s, %s (%s)' % (
            self.song.song_name, self.entertainer.last_name, self.entertainer.first_name, self.role)

    def get_absolute_url(self):
        return reverse('fandom_create_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_create_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_create_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['song', 'role', 'entertainer']
        constraints = [UniqueConstraint(fields=['song', 'role', 'entertainer'], name='unique_create')]


class EventCategory(models.Model):
    event_cat_id = models.AutoField(primary_key=True)
    event_cat_name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return '%s' % self.event_cat_name

    class Meta:
        ordering = ['event_cat_name']


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=45)
    disambiguator = models.CharField(max_length=45, blank=True, default='')
    style = models.ForeignKey(Style, related_name='event', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        result = ''
        if self.disambiguator == '':
            result = '%s' % self.event_name
        else:
            result = '%s (%s)' % (self.event_name, self.disambiguator)
        return result

    def get_absolute_url(self):
        return reverse('fandom_event_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_event_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_event_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['event_name', 'disambiguator']
        constraints = [
            UniqueConstraint(fields=['event_name', 'disambiguator'], name='unique_event')
        ]


class Activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, related_name='activity', on_delete=models.PROTECT)
    entertainer = models.ForeignKey(Entertainer, related_name='activity', on_delete=models.PROTECT)
    activity_date = models.DateField()
    role = models.ForeignKey(Role, related_name='activity', on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s - %s, %s (%s)' % (self.activity_date, self.event.event_name,
                                        self.entertainer.last_name, self.entertainer.first_name, self.role)

    def get_absolute_url(self):
        return reverse('fandom_activity_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('fandom_activity_update_urlpattern',
                       kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('fandom_activity_delete_urlpattern',
                       kwargs={'pk': self.pk})

    class Meta:
        ordering = ['event', 'activity_date', 'entertainer']
        constraints = [
            UniqueConstraint(fields=['event', 'activity_date', 'entertainer'], name='unique_activate')
        ]



