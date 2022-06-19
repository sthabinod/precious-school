# Generated by Django 4.0.5 on 2022-06-19 04:02

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='profile/', verbose_name='Profile Picture')),
                ('status', models.CharField(choices=[('ACTIVE', 'active'), ('INACTIVE', 'inactive')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]