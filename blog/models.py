from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.text import slugify



# Create your models here.
class Profile(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'), ('F', 'Female')
		)

	user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="profile")
	middle_name = models.CharField(max_length=30, blank=True)
	gender =  models.CharField(max_length=1, choices=GENDER_CHOICES)
	birth_date = models.DateField(blank=True, null=True)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

	@receiver(post_save, sender=User)
	def update_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)
		instance.profile.save()


class Post(models.Model):
	STATUS = (
		(0, 'Draft'), (1, 'Publish')
		)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(max_length=200, unique=True)
	body = models.TextField()
	status = models.IntegerField(choices=STATUS, default=0)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField()

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='post')
	body = models.TextField()
	date_created = models.DateTimeField(auto_now_add=True)
