# Generated by Django 3.2.5 on 2021-08-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0017_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='store/pdfs/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='store/covers/')),
            ],
        ),
    ]