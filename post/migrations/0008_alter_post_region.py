# Generated by Django 5.0.6 on 2024-05-11 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='post.region'),
        ),
    ]
