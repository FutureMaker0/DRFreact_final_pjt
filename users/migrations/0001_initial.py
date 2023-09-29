# Generated by Django 3.1.6 on 2023-09-29 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0014_alter_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('nickname', models.CharField(max_length=128)),
                ('position', models.CharField(max_length=128)),
                ('subjects', models.CharField(max_length=128)),
                ('image', models.ImageField(default='default.png', upload_to='profile/')),
            ],
        ),
    ]
