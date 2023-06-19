from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_userprofile_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_admin',
        ),
    ]