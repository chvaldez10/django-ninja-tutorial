# Generated by Django 5.0 on 2024-09-02 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waitlists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='waitlistentry',
            old_name='emails',
            new_name='email',
        ),
    ]
