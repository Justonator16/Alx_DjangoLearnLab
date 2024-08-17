from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20 )

    def __str__(self):
        return self.name

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
    books = models.ManyToManyField(Book,  )

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

    user = models.OneToOneField(User, on_delete=models.CASCADE)
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


# record = Author(name="Junior")
# record.save()

# b = Book(title="1987", author=record)
# b.save()

# print(b.author.id)
# print(b.author)
