# Generated by Django 4.2.7 on 2023-12-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_contract_group_musiciancontractstatus_organizer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Group',
            new_name='Bike',
        ),
        migrations.DeleteModel(
            name='Musician',
        ),
        migrations.RenameField(
            model_name='bike',
            old_name='date_started',
            new_name='brand',
        ),
    ]
