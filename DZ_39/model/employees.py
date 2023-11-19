from model.datadase import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Employees(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    departments = Column(Integer, ForeignKey("departments.id"))

    def __init__(self, full_name, age, departments):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.departments = departments

    def __repr__(self):
        return f'Сотрудники (ФИО: {self.surname} {self.name} {self.patronymic}), возраст: {self.age},' \
               f' ID_отдела: {self.departments}'
