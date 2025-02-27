# Generated by Django 5.1.3 on 2024-11-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField()),
                ('alternative_mobile_number', models.IntegerField()),
                ('permanent_address', models.CharField(max_length=80)),
                ('working_address', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Educationdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField()),
                ('qualification', models.CharField(max_length=40)),
                ('occupations', models.CharField(max_length=40)),
                ('annual_income', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Familydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=40)),
                ('mother_name', models.CharField(max_length=40)),
                ('sister_name', models.CharField(max_length=40)),
                ('about_family', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Partnerprefarencedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('looking_for', models.CharField(max_length=40)),
                ('caste', models.CharField(max_length=40)),
                ('qualification', models.CharField(max_length=40)),
                ('occupations', models.CharField(max_length=40)),
            ],
        ),
    ]
