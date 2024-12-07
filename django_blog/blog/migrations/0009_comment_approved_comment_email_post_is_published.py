# Generated by Django 5.1.2 on 2024-11-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]