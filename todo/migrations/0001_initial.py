# Generated by Django 3.0.4 on 2020-03-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('description', models.TextField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]