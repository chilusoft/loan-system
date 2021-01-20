# Generated by Django 3.1.5 on 2021-01-20 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_id_num', models.IntegerField()),
                ('DOB', models.DateField(verbose_name='Date of birth')),
                ('DOR', models.DateTimeField(auto_now_add=True, verbose_name='Date of registration')),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OccupationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_employer', models.CharField(max_length=255)),
                ('employer_address', models.TextField()),
                ('job_title', models.CharField(max_length=255)),
                ('employee_num', models.CharField(max_length=32)),
                ('date_of_eng', models.DateTimeField(verbose_name='Date of Engagement')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customerinformation')),
            ],
        ),
        migrations.CreateModel(
            name='LoanDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.FloatField(default=0)),
                ('interest_rate', models.FloatField(choices=[(0.15, '15%'), (0.25, '25%'), (0.35, '35%')], default=0.25)),
                ('date_of_request', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.customerinformation')),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.occupationdetails')),
            ],
        ),
    ]