# Generated by Django 4.2.2 on 2024-11-05 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0007_alter_usefulhabit_time_to_complete'),
    ]

    operations = [
        migrations.CreateModel(
            name='PleasantHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='название приятной привычки')),
            ],
        ),
        migrations.AlterField(
            model_name='usefulhabit',
            name='pleasant_habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pleasant_habit', to='habits.pleasanthabit', verbose_name='приятная привычка'),
        ),
    ]
