from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from LibraryProject import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20 )

    def __str__(self):
        return self.name
    
    # class Meta:
    #     permissions = [
    #         ("can_view", "Can view instance"),
    #         ("can_create", "Can create instance"),
    #         ("can_edit", "Can edit instance"),
    #         ("can_delete", "Can delete instance"),
    #     ]

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,  )

    def __str__(self):
        return f"{self.title} by {self.author}"
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]
    
class Library(models.Model):
    name = models.CharField(max_length=20,  )
    books = models.ManyToManyField(Book )

    def __str__(self):
        return f"Library name {self.name} {self.books} "
    
class Librarian(models.Model):
    name = models.CharField(max_length=20,  )
    library = models.OneToOneField(Library, on_delete=models.CASCADE,  )

    def __str__(self):
        return f"Librarian name {self.name} , Library {self.library}"

class UserProfile(models.Model):
    role_choices = [('Admin','Admin'),
                    ('Librarian', 'Librarian'),
                    ('Member', 'Member'),
                    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=role_choices)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password)

# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField(null=True, blank=True)
#     profile_photo = models.ImageField()

#     objects = CustomUserManager()
#     def __str__(self) -> str:
#         return self.username

