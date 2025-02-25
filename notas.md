# Puntos para la entrega final

- Entrega individual
- subir a github
- readme como la entrega 3
- video de maximo 10 min que muestre la pagina y sus funcionalidades (con o sin audio)
  - programas que pueden utilizar freecam8, obs, filmora 12, etc.
- No agregar la Base de datos (el archivo db.sqlite3) en la entrega. Deberia estar en el .gitignore
- Uso de herencia de templates
- Exista gitignore con:
```
<carpeta del entorno virtual>
__pycache__
db.sqlite3
media
```

Estos ultimos son por el hecho de no compartir la info de tu bd y, aparte, las imagenes son archivos muy pesados que no es recomendable tenerlos en el repo. En cambio, las imagenes que sean parte del codigo del proyecto deberian guardarse en la carpeta static.

- Existencia del archivo requirements.txt actualizado.
- Tener en cuenta al manejar forms con imagenes hay que adaptar el template, y la vista...no solo el modelo y el formulario.
- Uso de minimo 2 clases basadas en vista.
- Uso de minimo un mixin en una CBV y un decorador en una view comun.
- Una vista de inicio
- acceso a una vista "Acerca de mi"/"About"
- Crear un modelo principal que contenga los siguiente campos como minimo: 3 Charfield  (o 2 Charfield y un Integerfield), 1 campo de imagen, 1 de fecha
- Vista de listado de los objetos del modelo principal (modelo a eleccion). En la cual cada objeto mostrara solo alguno de sus datos
- Mensaje que de aviso en caso de no haber ningun objeto creado o al utilizar el buscador no encontrar tampoco algun objeto
- Desde el listado:
    1. poder acceder a una vista que muestre el detalle de el objeto seleccionado
    2. poder acceder a una vista de creacion, una de edicion y una de borrado de los objetos del listado
- Registrar en el apartado de admin todos los modelos creados
- Tener una app para el manejo de todas las vistas relacionadas al usuario/autenticacion
- Desarrollar las vistas para un login, un logout y el registro de un usuario al cual se le solicite: username, email, password
- Crear una vista de perfil donde se muestren los datos del usuario:
  - nombre
  - apellido
  - email
  - avatar
  - Campo a eleccion (biografia, fecha de nacimiento, gustos, hobbies, etc)
- Desde el perfil, crear un acceso a una vista de edicion de estos datos.

- PUNTAZO A TENER EN CUENTA! PROBAR, PROBAR Y PROBAR ANTES DE
SUBIR EL CODIGO A GITHUB... ( no apurarse a hacer el commit y subir los
cambios porque puede generar algun problema sin darnos cuenta )