# Generated by Django 3.0.4 on 2020-04-10 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200410_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='users',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='blog.Post'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
