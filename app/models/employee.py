from sqlalchemy import Column, Date, Float, Integer, String

from database import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    puesto = Column(String, nullable=False)
    salario = Column(Float, nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
