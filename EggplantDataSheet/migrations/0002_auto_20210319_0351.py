# Generated by Django 3.1.7 on 2021-03-19 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EggplantDataSheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EggplantDataSheetDescription',
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
            model_name='eggplantdatasheet',
            name='plot_no',
        ),
        migrations.RemoveField(
            model_name='eggplantdatasheet',
            name='rep_no',
        ),
        migrations.AddField(
            model_name='eggplantdatasheet',
            name='description',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='EggplantDataSheet.eggplantdatasheetdescription'),
            preserve_default=False,
        ),
    ]