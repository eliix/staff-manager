from datetime import date

from pydantic import BaseModel


class EmployeeBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    puesto: str
    salario: float
    fecha_ingreso: date


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
