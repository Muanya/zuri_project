# Generated by Django 3.2 on 2021-04-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(null=True),
        ),
    ]
