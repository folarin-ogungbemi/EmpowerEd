# Generated by Django 3.2 on 2023-02-17 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('mentor_id', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.TextField()),
                ('area_of_expertise', models.CharField(max_length=255)),
                ('userpic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=20)),
                ('userpic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('role', models.CharField(choices=[('Mentor', 'Mentor'), ('Student', 'Student'), ('Parent', 'Parent')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('interests', models.TextField()),
                ('userpic', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.parent')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('relationship_id', models.AutoField(primary_key=True, serialize=False)),
                ('mentor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
        migrations.AddField(
            model_name='parent',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.AddField(
            model_name='mentor',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.user'),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]