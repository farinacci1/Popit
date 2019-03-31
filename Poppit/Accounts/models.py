from django.db import models

from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
)
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserManager(BaseUserManager):
	def create_user(self,email,password=None,is_active = True, is_staff = False,is_admin = False,is_confirmed = False):
		if not email:
			raise ValueError("Email adress is required")
		if not password:
			raise ValueError("Password is required")

		user_obj = self.model(
				email = self.normalize_email(email),
		)
		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.confirmed = is_confirmed
		user_obj.active = is_active
		user_obj.save(using=self._db)
		return user_obj
	def create_staffuser(self,email,password=None):
		user = self.create_user(
			email,
			password = password,
			is_staff = True
		)

		return user
	def create_superuser(self,email,password=None):
		user = self.create_user(
			email,
			password = password,
			is_staff = True,
			is_admin = True
		)
		return user

class User(AbstractBaseUser):
	email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)
	active = models.BooleanField(default = True) #login eligible
	staff = models.BooleanField(default = False) #staff non-super
	admin = models.BooleanField(default = False) #superuser
	confirmed = models.BooleanField(default = False) #superuser
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD ='email' #username

	REQUIRED_FIELDS =[]

	objects = UserManager()

	def __str__(self):
		return self.email
	def get_first_name(self):
		return self.first_name
	def get_last_name(self):
		return self.last_name
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True
	@property
	def is_staff(self):
		return self.staff
	@property
	def is_admin(self):
		return self.admin
	@property
	def is_active(self):
		return self.active
	@property
	def is_confirmed(self):
		return self.confirmed

GENDER_CHOICES = (
	('Ag','Agender'),
	('An','Androgynous'),
	('Bi','Bigender'),
	('Ma','Man'),
	('No','Nonbinary'),
	('Ot','Other'),
	('Pa','Pangender'),
	('Tr','Transgender'),
	('Un','Unspecified'),
	('Wo','Woman'),
)

class Profile(models.Model):
	user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
	profilePic = models.ImageField(blank=True,null=True)
	gender = models.CharField(max_length= 50, choices=GENDER_CHOICES, default='Un')
	birth_Date = models.DateField(null=True, blank=True)
	about = models.TextField(max_length=1000, blank=True)



	def create_profile(sender,  **kwargs):
	    if kwargs['created']:
	       profile = Profile.objects.create(user= kwargs['instance'])

	post_save.connect(create_profile, sender= User)
