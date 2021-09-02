# Generated by Django 3.2.6 on 2021-09-02 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_jobs_job_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='description',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='jobs',
            name='publish_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='salery',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='jobs',
            name='vacency',
            field=models.IntegerField(default=1),
        ),
    ]