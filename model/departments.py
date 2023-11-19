from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.datadase import Base


class Departments(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    department_number = Column(Integer, nullable=False)
    employee = relationship("Employees")

    # def __init__(self, department_number, employee):
    #     self.department_number = department_number
    #     self.employee = employee

    def __repr__(self):
        return f'Отдел: ( ID: {self.id}, Номер {self.department_number}, {self.employee})'
