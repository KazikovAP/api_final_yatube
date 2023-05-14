# Generated by Django 3.2.16 on 2023-05-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20230514_1906'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user_following',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='following',
            new_name='author',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'author'), name='user_author'),
        ),
    ]