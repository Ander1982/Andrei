from model.datadase import create_db1, Session
from model.employees import Employees
from model.departments import Departments
from faker import Faker


def create_database(load_fake_data1=True):
    create_db1()
    if load_fake_data1:
        _load_fake_data1(Session())


def _load_fake_data1(session: object):
    group1 = Departments(department_number=1)
    group2 = Departments(department_number=2)

    session.add(group1)
    session.add(group2)

    faker = Faker(locale='ru_RU')
    department_list = [group1, group2]
    session.commit()

    for _ in range(50):
        full_name = faker.name().split()
        age = faker.random.randint(25, 50)
        departments = faker.random.choice(department_list)
        employee = Employees(full_name, age, departments.id)
        session.add(employee)

    session.commit()
    session.close()
