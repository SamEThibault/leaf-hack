# Generated by Django 3.2.23 on 2024-02-03 20:15

from django.db import migrations, models
import django.db.models.deletion
import main.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('crop_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('crops', models.ManyToManyField(related_name='users', to='main.Crop')),
            ],
        ),
        migrations.CreateModel(
            name='Leaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, storage=main.models.S3Storage(), upload_to=main.models.leaf_image_upload_path)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('recommendations', models.ManyToManyField(related_name='leaves', to='main.Recommendation')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='leaves',
            field=models.ManyToManyField(related_name='crops', to='main.Leaf'),
        ),
    ]
