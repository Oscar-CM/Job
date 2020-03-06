# Generated by Django 3.0.3 on 2020-03-05 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobs', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('profile', models.TextField()),
                ('cv', models.FileField(upload_to='')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='jobs.Post')),
            ],
        ),
    ]