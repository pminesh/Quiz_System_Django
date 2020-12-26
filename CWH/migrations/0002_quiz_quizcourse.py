# Generated by Django 3.1.4 on 2020-12-23 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CWH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qustion', models.CharField(max_length=500)),
                ('option1', models.CharField(max_length=50)),
                ('option2', models.CharField(max_length=50)),
                ('option3', models.CharField(max_length=50)),
                ('option4', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=50)),
                ('quiz_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CWH.quizcourse')),
            ],
        ),
    ]