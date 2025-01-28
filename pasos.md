1. creamos una carpeta donde vamos a meter el proyecto
2. entramos en la carpeta y la abrimos con vscode
3. creamos el archivo .gitignore le guardamos lo generado por la pagina [gitignore.io](https://gitignore.io) seleccionando lo que van a utilizar (en nuestro caso `visualstudiocode`, `python` y `django`)
4. creamos el entorno virtual `python -m venv <nombre_de_la_carpeta_que_contiene_el_entorno_virtual>` (`*`)
5. agregar el nombre del entonrno virtual al .gitignore (`*`)
6. inicializamos git
7. creamos el primer commit
8. conectamos nuestro repositorio con el repositorio en la nube (github u otro)
9. hacemos el primer push
10. activamos el entorno virtual (`*`)
11. instalar django con el manejador de paquetes de python `pip` con el comando `pip install Django`
12. crear el requirements.txt con los datos de las dependencias usando el comando `pip freeze > requirements.txt` (`**`)
13. crear el proyecto django donde estamos trabajando con el comando `django-admin startproject <nombre_del_proyecto> .` (`***`)
14. probamos el proyecto ejecutando primero `python manage.py migrate` y luego `python manage.py runserver`
15. creamos nuestra app principal con el comando `python manage.py startapp <nombre_de_la_app>`
    - agregamos la app a el archivo settings.py
    - creamos el archivo urls.py dentro de nuestra app
    - agregamos el path que conecta al urls.py de la carpeta donde esta el settings.py al de nuestra app con el codigo `path('<url_que_quieran_poner>', include('<nombre_de_la_app>.urls'))`
16. agregamos el valor `BASE_DIR / 'templates'` a la lista en la key `DIRS` de la variable `TEMPLATES` en el archivo settings.py
17. creamos la carpeta templates a la altura de las apps
18. crear un super usuario que nos permita acceder al apartado de admin de nuestra pagina ejecutando `python manage.py createsuperuser`
    - tener en cuenta que cuando se solicita la password cuando escriben no se muestra en la terminal pero se esta escribiendo igual (esto es para que no se vea la password que estan configurando a modo de seguridad)
19. crear vistas
    - crear el path que conectara con su vista en el archivo `urls.py` de la app que corresponda
    - crear la vista en el archivo `views.py` de la app que corresponda
    - crear el template que utilizaran para la vista dentro de la carpeta templates
    - agregar el link (etiqueta `a`) al path que corresponde a la vista
20. crear modelos
    1. crear modelo dentro de el archivo `models.py`
        - heredan de `models.Model`
        - los atributos los completan con los Fields que les brinda `models` ejemplo `models.CharField(max_length=20)`
    2. generar una migracion con el comando `python manage.py makemigrations`
    3. plasmar la migracion en la bd con el comando `python manage.py migrate`
    4. En caso de modificacion de un modelo existente, creacion de otro modelo o borrado de un modelo volver a ejecutar los pasos 2 y 3
        - tener en cuenta que para modificar el nombre y los atributos de un mismo modelo se deben hacer los pasos 2 y 3 una vez por la modificacion de los atributos y otro por el cambio en el nombre del modelo para no generar conflictos con django
    5. registrar el modelo en el apartado de admin importando en el archivo `admin.py` el modelo y agregando el codigo `admin.site.register(<modelo_importado>)`
        - en caso de ser varios modelos se puede agregar esta ultima linea para cada modelo o hacer una sola linea y pasarle todos los modelos dentro de una lista
    6. importar el modelo creado en el views.py que corresponda para utilizarlo en las vistas
21. crear formularios
    1. crear el archivo `forms.py` dentro de la app que corresponda en caso que no este creado
    2. crear el formulario
        - heredan de `forms.Form`
        - los atributos los completan con los Fields que les brinda `forms` ejemplo `forms.CharField(max_length=20)` (`****`)
    3. importar el formulario creado en el views.py que corresponda para utilizarlo en las vistas

(`*`) En caso de no utilizar entorno virtual omitir este paso  
(`**`) Este paso se debe repetir tras cada instalacion de paquetes para mantener la informacion actualizada  
(`***`) No olvidar el punto al final para que les genere el proyecto donde estan parados y no se creen carpetas de mas  
(`****`) Como veran es muy similar a lo que se hace en los modelos (no es exactamente igual para todo)  
