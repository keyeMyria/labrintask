# Generated by Django 2.1 on 2018-08-16 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(upload_to='users/image', verbose_name='Image')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_photo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
