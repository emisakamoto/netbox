from django.db import migrations

from utilities.ordering import naturalize_interface

def rename_interface_naturalize(apps, schema_editor):
    """
    Rename the '_name' field in the database for interfaces. Fixes the ordering.
    """
    Interface = apps.get_model('dcim', 'Interface')
    interfaces = Interface.objects.all()

    for interface in interfaces:
        interface._name = naturalize_interface(interface.name, max_length=100)

    Interface.objects.bulk_update(interfaces, ['_name'], batch_size=100)

class Migration(migrations.Migration):
    dependencies = [
        ('dcim', '0181_rename_device_role_device_role'),
    ]

    operations = [
        migrations.RunPython(
            code=rename_interface_naturalize,
            reverse_code=migrations.RunPython.noop
        ),   
    ]
