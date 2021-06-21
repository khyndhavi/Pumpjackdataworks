from csv import DictReader
from db.db_operations import DBOperations


def read_file_and_update_database_print_details(file_name):
    with open('flat_data.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        records = DictReader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in records:
            first_name = row['first_name']
            last_name = row['last_name']
            salary = row['salary']
            department_name = row['dept_name']
            salary_increment = row['salary_increment']
            dept_id = DBOperations.get_department_id(department_name)
            if not dept_id:
                DBOperations.insert_into_department_table(department_name, salary_increment)
                dept_id = DBOperations.get_department_id(department_name)
                if dept_id:
                    employee_id = DBOperations.get_employee_id(first_name, last_name)
                    if not employee_id:
                        DBOperations.insert_into_employee_table(first_name, last_name, salary, dept_id)
                    else:
                        print("Employee with name:{} record already exist and not inserting record".format(first_name))
                else:
                    print("Failed in inserting the department and skipping inserting the employee record..")
            else:
                DBOperations.insert_into_employee_table(first_name, last_name, salary, dept_id)

    DBOperations.print_employee_updated_salary()


if __name__ == '__main__':
    read_file_and_update_database_print_details("flat_data.csv")


