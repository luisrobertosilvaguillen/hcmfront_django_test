**Configurar Credenciales PostgreSql (BDNAME, USERNAME, PASSWORD)**

 	Archivo Settings.py, Lineas 82,83,84

**Migrar Base de Datos**

 	manage.py migrate

**Cargar Data Inicial**

 	manage.py loaddata group
	
	manage.py loaddata user
	
 	manage.py loaddata reservation_priority
	
 	manage.py loaddata reservation_status
	
 	manage.py loaddata supply

**Iniciar Servidor**
 	manage.py runserver

**Ingresar con el las credenciales de usuario administrador**

 	usuario:admin
	
 	password:admin

**Uso de la aplicación** 
 
 1. Modulo Usuario: Cargar usuarios (roles = admin y general) para las pruebas funcionales
 
	Nota: Para efectos de la prueba no se desarrollo la edicion de usuarios, ni recuperación de contraseña.

 2. Modulo Insumos: Cargar Insumos (Estarán disponibles para la creación de Salas de Reuniones)
 
 3. Modulo Salas de Reuniones: Cargar Salas de Reuniones (Nombre, Ubicación, Horario, Capacidad, Insumos)

	LOS PASOS ANTERIORES SOLO LOS HACE UN USUARIO ADMIN

 4. Ingresar con Usuario General (CREAR RESERVACIONES, SOLICITAR RESERVACIONES DE OTRO USUARIO SI LAS HAY, CONFIRMAR LA RESERVACION)
 
	Nota: El usuario que crea la reservación debe confirmarla según las siguientes reglas
	
		RESERVACION PRIORIDAD NORMAL: SOLO PUEDE CONFIRMAR ENTRE LAS ULTIMAS 8 HORAS ANTES DE LA RESERVACION
		
		RESERVACION PRIORIDAD INORTANTE: PUEDE CONFIRMAR INMEDITAMENTE SEA CREADA LA RESERVACION
 

 5. Ingresar con Usuario Admin (EDITAR RESERVACIONES, ELIMINAR RESERVACIONES, DECIDIR SI CEDE UNA RESERVACION A OTRO USUARIO O NO EN CASO DE QUE HAYAN PETICIONES PENDIENTES)

 
**Feedback**

 Para la resolucion del problema use algunas cosas que no estaban en el enunciado tales como:
 
 Estatus de Prioridad de una reservación (Determina si se puede confirmar la reservación inmediatamente o entre las ultimas 8 horas antes de la misma, esto con la finalidad de que si extistiese una reunion de caracter importante, pueda solicitar una reservacion con estatus reservada y aun no confirmada)
	
 Manejo básico de notificaciones (Para un mejor manejo de las solitudes de reservaciones, avisar al empleado si su reservacion fue eliminada, ademas si la reservacion fue asignada a otro usuario)
 
 Hice uso de vistas basadas en funciones y vistas basadas en clases con el fin de demostrar el conocimiento en ambos aspectos, no por ser desornedado :)
 
 Me esforce en el diseño, maquetado e interactividad del proyecto con el fin de hacerlo amigable al usuario.
 
 Espero sea de su agrado. Saludos!
