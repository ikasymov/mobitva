# Generated by Django 2.0.3 on 2018-03-25 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_location_passages'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travelers', to='api.Location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pathways', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='attribute',
            name='arsenal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='api.Arsenal'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='api.Action'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userarsenal',
            name='arsenal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.Arsenal'),
        ),
        migrations.AlterField(
            model_name='userarsenal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arsenals', to=settings.AUTH_USER_MODEL),
        ),
    ]
