# Generated by Django 5.1.4 on 2024-12-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_alter_voices_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='voices',
            name='deneme',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
