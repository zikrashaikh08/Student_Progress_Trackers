# Generated by Django 3.0.7 on 2021-10-13 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curricular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('certificate', models.FileField(upload_to='')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Students')),
            ],
        ),
    ]
