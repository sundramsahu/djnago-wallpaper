# Generated by Django 3.2.4 on 2021-07-26 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='photo',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='photos.category'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]