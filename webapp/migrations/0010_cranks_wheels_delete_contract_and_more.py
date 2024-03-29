# Generated by Django 4.2.7 on 2023-12-10 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_frames_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cranks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('Size', models.DateField(auto_now_add=True)),
                ('media_file', models.FileField(blank=True, upload_to='wheels/')),
            ],
        ),
        migrations.CreateModel(
            name='Wheels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('description', models.TextField(blank=True)),
                ('Size', models.DateField(auto_now_add=True)),
                ('media_file', models.FileField(blank=True, upload_to='wheels/')),
            ],
        ),
        migrations.DeleteModel(
            name='Contract',
        ),
        migrations.DeleteModel(
            name='MusicianContractStatus',
        ),
        migrations.DeleteModel(
            name='Organizer',
        ),
        migrations.DeleteModel(
            name='Track',
        ),
        migrations.AlterField(
            model_name='frames',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Frames/'),
        ),
        migrations.AlterField(
            model_name='handlebars',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Handlebars/'),
        ),
    ]
