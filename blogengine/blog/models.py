from django.db import models
from django.shortcuts import reverse

from django.utils.text import slugify
from time import time

from django.contrib.auth.models import User


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length = 150, db_index = True)
    slug = models.SlugField(max_length = 150, unique=True, blank = True)
    body = models.TextField(blank = True, db_index = True)
    tags = models.ManyToManyField('Tag', blank = True, related_name='posts')
    date_pub = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})


    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug':self.slug})


    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug':self.slug})


class Tag(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(max_length = 50, unique = True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})


    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug':self.slug})


    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug':self.slug})



class Comment(models.Model):
    user = models.CharField(max_length = 20, default = None)
    body = models.TextField(max_length=500)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.SET_NULL, null=True, default = None)
    date_pub = models.DateTimeField(auto_now_add=True)


    def __str__():
        return self.body


    class Meta:
        ordering = ['-date_pub']
