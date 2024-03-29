# Generated by Django 4.2.7 on 2024-01-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_cranks_wheels_handlebars_frames_wheels_handlebars_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='Bname',
            new_name='bname',
        ),
        migrations.RenameField(
            model_name='cranks',
            old_name='Cname',
            new_name='cname',
        ),
        migrations.RenameField(
            model_name='cranks',
            old_name='Size',
            new_name='sze',
        ),
        migrations.RenameField(
            model_name='frames',
            old_name='Fname',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='handlebars',
            old_name='Hname',
            new_name='hname',
        ),
        migrations.RenameField(
            model_name='wheels',
            old_name='Size',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='wheels',
            old_name='Wname',
            new_name='wname',
        ),
        migrations.RemoveField(
            model_name='handlebars',
            name='Types',
        ),
        migrations.AddField(
            model_name='handlebars',
            name='types',
            field=models.TextField(blank=True),
        ),
    ]
