
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='recommend',
            field=models.BooleanField(default=False, verbose_name='是否推荐'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='a_content',
            field=models.CharField(max_length=3000, null=True, verbose_name='公告内容'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='a_title',
            field=models.CharField(max_length=64, verbose_name='公告标题'),
        ),
    ]
