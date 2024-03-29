# Generated by Django 4.2.7 on 2024-01-14 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_bike_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cranks',
            name='HandleBars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.handlebars'),
        ),
        migrations.AddField(
            model_name='frames',
            name='bike',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.bike'),
        ),
        migrations.AddField(
            model_name='handlebars',
            name='frames',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.frames'),
        ),
        migrations.AddField(
            model_name='wheels',
            name='HandleBars',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapp.handlebars'),
        ),
    ]
