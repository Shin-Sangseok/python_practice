from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_writer',
            field=models.CharField(default='blank', max_length=500),
        ),
    ]