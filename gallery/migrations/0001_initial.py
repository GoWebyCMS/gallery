# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image_file', filer.fields.image.FilerImageField(to='filer.Image')),
                ('obj', models.ForeignKey(to='gallery.Gallery')),
            ],
        ),
        migrations.AddField(
            model_name='gallery',
            name='featured_image',
            field=filer.fields.image.FilerImageField(to='filer.Image', related_name='featured'),
        ),
    ]
