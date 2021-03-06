# Generated by Django 2.1.7 on 2019-03-06 03:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LabeledData',
            fields=[
                ('labeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_content', models.CharField(max_length=100)),
                ('labeled_time', models.DateTimeField()),
                ('labeled_content', models.CharField(max_length=120)),
                ('predicted_relation', models.CharField(max_length=20)),
                ('predicted_e1', models.CharField(max_length=20)),
                ('predicted_e2', models.CharField(max_length=20)),
                ('labeled_relation', models.CharField(max_length=20)),
                ('labeled_e1', models.CharField(max_length=20)),
                ('labeled_e2', models.CharField(max_length=20)),
                ('additional_info', models.CharField(max_length=30)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.File')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=20, unique=True)),
                ('project_tags', models.TextField()),
                ('sentence_labeled', models.IntegerField(default=0)),
                ('sentence_unlabeled', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UnLabeledData',
            fields=[
                ('unlabeled_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_content', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField()),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.File')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.Project')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='labeleddata',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.Project'),
        ),
        migrations.AddField(
            model_name='file',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='annotator.Project'),
        ),
    ]
