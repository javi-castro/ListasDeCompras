<<<<<<< HEAD
#!/usr/bin/env python ---
#Hola me llamo Felipe Vera
=======
#!/usr/bin/env python
>>>>>>> 56430b9eb8b05f339ccf7aa41424f3b912b7c2c1
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
