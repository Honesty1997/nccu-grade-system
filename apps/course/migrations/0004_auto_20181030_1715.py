# Generated by Django 2.0 on 2018-10-30 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20181028_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.Teacher'),
        ),
    ]
