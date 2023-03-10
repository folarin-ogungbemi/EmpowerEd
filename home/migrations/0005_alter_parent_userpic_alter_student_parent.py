# Generated by Django 4.1.1 on 2023-02-19 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_parent_userpic_alter_student_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='userpic',
            field=models.CharField(blank=True, default='https://i.imgur.com/0ndtScF.png', max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='parent',
            field=models.ForeignKey(blank=True, default='https://i.imgur.com/0ndtScF.png', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.parent'),
        ),
    ]
