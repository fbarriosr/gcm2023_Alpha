from django.core.management.base import BaseCommand
from usuarios.models import Usuario

class Command(BaseCommand):
    help = 'Cambia todas las contraseñas de los usuarios, excepto para ciertos perfiles'

    def handle(self, *args, **kwargs):
        nueva_contraseña = "cgm2024"
        
        # Perfiles que deben ser excluidos
        perfiles_excluidos = ['SUPER']
        
        # Filtrar usuarios que no tienen los perfiles excluidos
        usuarios = Usuario.objects.exclude(perfil__in=perfiles_excluidos)
        total_usuarios = usuarios.count()
        
        for usuario in usuarios:
            usuario.set_password(nueva_contraseña)
            usuario.save()

        self.stdout.write(self.style.SUCCESS(
            f'Se han actualizado las contraseñas de {total_usuarios} usuarios. Perfiles excluidos: {perfiles_excluidos}'
        ))


#docker-compose exec web python manage.py reset_passwords