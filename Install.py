import subprocess

nom_module = 'selenium'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'colorama'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'time'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'requests'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'json'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'random'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

nom_module = 'string'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")
    
nom_module = 'ctypes'
try:
        subprocess.check_call(['pip', 'install', nom_module])
        print(f"Le module {nom_module} a été installé avec succès.")
except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'installation du module {nom_module}. Code d'erreur : {e.returncode}")

from Programmes.Options.Options import Reset

Reset()