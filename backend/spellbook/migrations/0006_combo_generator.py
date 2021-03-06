# Generated by Django 4.0.6 on 2022-07-19 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spellbook', '0005_alter_variant_status'),
    ]

    def forward_func(apps, schema_editor):
        Combo = apps.get_model('spellbook', 'Combo')
        for combo in Combo.objects.all():
            combo.generator = len(combo.includes.all()) + len(combo.needs.all()) > 1
            combo.save()

    operations = [
        migrations.AddField(
            model_name='combo',
            name='generator',
            field=models.BooleanField(default=True, help_text='Is this combo a generator for variants?', verbose_name='is generator'),
        ),
        migrations.RunPython(
            forward_func,
            migrations.RunPython.noop,
            elidable=True
        )
    ]
