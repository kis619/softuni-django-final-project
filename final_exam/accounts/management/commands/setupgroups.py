from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Sets up the initial groups and permissions'

    def handle(self, *args, **options):
        staff_group, created = Group.objects.get_or_create(name='Staff')
        staff_group.permissions.add(*Permission.objects.filter(codename__in=['view_post', 'delete_post']))
        superuser_group, created = Group.objects.get_or_create(name='Superusers')
