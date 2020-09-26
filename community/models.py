from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag_set = models.ManyToManyField('Tag', blank=True)
    message = models.TextField(
        validators=[MinLengthValidator(5)]
    )
    photo = models.ImageField(blank=True, upload_to='community/post')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('community:post_detail', args=[self.pk])

    def add_view(self):
        self.view += 1
        self.save()

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length = 50, unique= True)

    def __str__(self):
        return self.name