

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='a_id',
        ),
        migrations.RemoveField(
            model_name='kind',
            name='k_id',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='t_id',
        ),
    ]
