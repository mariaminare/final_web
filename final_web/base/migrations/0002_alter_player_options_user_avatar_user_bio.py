# Generated by Django 5.0.7 on 2024-07-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
