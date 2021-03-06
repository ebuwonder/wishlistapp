# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-30 20:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
        migrations.AddField(
            model_name='items',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='wishlist.Users'),
        ),
        migrations.AddField(
            model_name='items',
            name='user',
            field=models.ManyToManyField(related_name='items', to='wishlist.Users'),
        ),
    ]
