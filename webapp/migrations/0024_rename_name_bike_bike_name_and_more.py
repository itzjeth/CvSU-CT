# Generated by Django 4.2.7 on 2024-01-16 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_rename_bname_bike_name_rename_cname_cranks_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='name',
            new_name='bike_name',
        ),
        migrations.RenameField(
            model_name='cranks',
            old_name='name',
            new_name='crank_name',
        ),
        migrations.RenameField(
            model_name='frames',
            old_name='name',
            new_name='frame_name',
        ),
        migrations.RenameField(
            model_name='handlebars',
            old_name='name',
            new_name='handlebar_name',
        ),
        migrations.RenameField(
            model_name='wheels',
            old_name='name',
            new_name='wheel_name',
        ),
    ]
