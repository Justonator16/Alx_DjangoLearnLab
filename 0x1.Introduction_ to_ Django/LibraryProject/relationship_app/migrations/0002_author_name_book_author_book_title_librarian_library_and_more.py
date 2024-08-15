# Generated by Django 5.0.7 on 2024-08-15 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='relationship_app.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='librarian',
            name='library',
            field=models.OneToOneField(default='N/A', on_delete=django.db.models.deletion.CASCADE, to='relationship_app.library'),
        ),
        migrations.AddField(
            model_name='librarian',
            name='name',
            field=models.CharField(default='N/A', max_length=20),
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(default='N/A', to='relationship_app.book'),
        ),
        migrations.AddField(
            model_name='library',
            name='name',
            field=models.CharField(default='N/A', max_length=20),
        ),
    ]
