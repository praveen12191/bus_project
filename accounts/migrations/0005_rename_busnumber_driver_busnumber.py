# Generated by Django 4.1.5 on 2023-03-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_studentname_student_rno'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='busNumber',
            new_name='busnumber',
        ),
    ]