# Generated by Django 3.1.7 on 2021-03-19 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SweetPotatoDataSheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SweetPotatoDataSheetDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('planting_date', models.DateField()),
                ('sowing_date', models.DateField()),
                ('accession_no', models.CharField(max_length=50)),
                ('plot_no', models.IntegerField()),
                ('curator', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='accession_no',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='curator',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='location',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='planting_date',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='plot_no',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='sowing_date',
        ),
        migrations.RemoveField(
            model_name='sweetpotatodatasheet',
            name='species',
        ),
        migrations.AddField(
            model_name='sweetpotatodatasheet',
            name='plant_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sweetpotatodatasheet',
            name='description',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SweetPotatoDataSheet.sweetpotatodatasheetdescription'),
            preserve_default=False,
        ),
    ]
