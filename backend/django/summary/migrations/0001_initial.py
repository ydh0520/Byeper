# Generated by Django 2.2 on 2020-11-12 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('video_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=80)),
                ('video_description', models.TextField()),
                ('video_img', models.TextField()),
                ('video_max_img', models.IntegerField()),
                ('video_file', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.TextField()),
                ('problem', models.TextField()),
                ('answer', models.CharField(max_length=100, null=True)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='summary.Video')),
            ],
        ),
    ]
