# Generated by Django 3.2.7 on 2021-09-10 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camera',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.site'),
        ),
        migrations.AlterField(
            model_name='site',
            name='s_sec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sousecteurs'),
        ),
        migrations.AlterField(
            model_name='sousecteurs',
            name='secteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.secteurs'),
        ),
    ]
