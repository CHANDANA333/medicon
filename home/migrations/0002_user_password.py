# Generated by Django 4.0.6 on 2023-08-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='pwd', max_length=100),
            preserve_default=False,
        ),
    ]