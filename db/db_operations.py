from db.db_connection import DBConnection


class DBOperations(object):

    @staticmethod
    def insert_into_department_table(dept_name, salary_inc):
        insert_query = "INSERT INTO department (department_name,salary_increment) VALUES (%s, %s)"
        params = (dept_name, salary_inc)
        result = DBConnection().execute_insert_query(insert_query, params)

    @staticmethod
    def insert_into_employee_table(first_name, last_name, salary, dept_id):
        insert_query = "INSERT INTO employee (first_name, last_name, salary, department_id) VALUES (%s, %s, %s, %s)"
        params = (first_name, last_name, salary, dept_id)
        result = DBConnection().execute_insert_query(insert_query, params)

    @staticmethod
    def get_department_id(dept_name):
        select_query = "select id from department where department_name = %s"
        params = (dept_name,)
        (result, row_count) = DBConnection().execute_select_query(select_query, params)
        if result and row_count > 0:
            print(result[0]['id'])
            return result[0]['id']
        else:
            return None

    @staticmethod
    def get_employee_id(first_name, last_name):
        select_query = "select id from employee where first_name = %s and last_name= %s"
        params = (first_name, last_name)
        (result, row_count) = DBConnection().execute_select_query(select_query, params)
        if result and row_count > 0:
            print(result[0]['id'])
            return result[0]['id']
        else:
            return None

    @staticmethod
    def print_employee_updated_salary():
        salary_query = "select e.id as employee_id, round(e.salary + (e.salary * d.salary_increment / 100)) as updated_salary from employee e, department d where e.department_id = d.id"
        (result, row_count) = DBConnection().execute_select_query(salary_query)
        print('employee_id, updated_salary')
        for row in result:
            print(str(row['employee_id']) + ", " + str(row['updated_salary']))
