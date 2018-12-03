#Hola me llamo Felipe Vera
#Hola mundo
<<<<<<< HEAD
#Cambio Prueba
#Prueba final a trabajar
#Prueba Final 2
=======
>>>>>>> PRUEBA CL
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ListaDeCompras.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
