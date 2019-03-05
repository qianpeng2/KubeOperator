# Generated by Django 2.1.2 on 2019-03-04 07:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('openshift_api', '0002_setting'),
    ]

    def forwards_func(apps, schema_editor):
        Setting = apps.get_model("openshift_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).bulk_create([
            Setting(name="主机名", key="hostname", order=0, value="", helper="eg:example.com"),
        ])

    def reverse_func(apps, schema_editor):
        Setting = apps.get_model("openshift_api", "Setting")
        db_alias = schema_editor.connection.alias
        Setting.objects.using(db_alias).filter(key='hostname').delete()

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]