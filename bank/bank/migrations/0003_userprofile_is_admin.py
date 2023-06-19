from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]