# Generated by Django 2.0.5 on 2018-05-13 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.SmallIntegerField(choices=[(0, 'pending'), (1, 'approved')], default=0)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'default_related_name': 'profiles',
            },
        ),
    ]
