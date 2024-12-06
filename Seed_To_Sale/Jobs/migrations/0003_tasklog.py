# Generated by Django 5.0.4 on 2024-12-06 20:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0001_initial'),
        ('Jobs', '0002_job_job_create_date_alter_job_job_start'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLog',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_tstamp', models.DateTimeField(auto_now_add=True)),
                ('task_data', models.JSONField()),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employee')),
                ('task_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jobs.job')),
            ],
        ),
    ]
