# Generated by Django 3.0.4 on 2020-03-10 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_profile_picture'),
        ('tweets', '0003_auto_20200310_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile', to_field='user'),
        ),
    ]
