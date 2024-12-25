# Generated by Django 5.1.4 on 2024-12-21 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0006_alter_voices_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voices',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voices', to='mainpage.users'),
            preserve_default=False,
        ),
    ]