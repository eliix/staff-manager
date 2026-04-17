# StaffManager 💼

API REST para la gestión de empleados desarrollada con FastAPI. Permite realizar operaciones CRUD, autenticación con JWT y consultas adicionales como estadísticas salariales y antigüedad.

## Tecnologías utilizadas

- FastAPI 
- PostgreSQL (con SQL alchemy)
- JWT
- Pytest 
- Pydantic 

## Modelo de empleado

Cada empleado contiene los siguientes campos:

`id`
`nombre`
`apellido`
`email`
`puesto`
`salario`
`fecha_ingreso`

## Autenticación

Endpoints básicos:

`POST /auth/register` -> Registro de usuario
`POST /auth/login` -> Login y obtención de token

## Endpoints

### CRUD de empleados
- `POST /employees`
    - Crear un nuevo empleado
- `GET /employees`
    - Listar empleados
Permite:
Filtrar por puesto
Paginación (page, limit)

- `GET /employees/{id}`
    - Obtener un empleado por ID
- `PUT /employees/{id}`
    - Actualizar un empleado
- `DELETE /employees/{id}`
    - Eliminar un empleado

### Endpoints adicionales

- `GET /employees/salary-average`
    - Devuelve el salario promedio de todos los empleados
- `GET /employees/salary-by-role`
    - Devuelve el salario promedio agrupado por puesto
- `GET /employees/{id}/seniority`
    - Calcula la antigüedad del empleado desde su fecha de ingreso

## Testing

Implementarlo con pytest
- testing de endpoints
- testing de lógica
- manejo de DB en tests
  
#### CRUD de empleados
- Crear empleado
- Obtener empleado
- Actualizar
- Eliminar
#### Auth (JWT)
- Login correcto
- Login incorrecto
- Acceso a endpoint protegido
