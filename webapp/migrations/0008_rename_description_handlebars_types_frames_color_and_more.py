# Generated by Django 4.2.7 on 2023-12-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_frames_handlebars_delete_parts_delete_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='handlebars',
            old_name='description',
            new_name='Types',
        ),
        migrations.AddField(
            model_name='frames',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='size',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='handlebars',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
