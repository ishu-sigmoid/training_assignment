import psycopg2
import logging
from openpyxl.workbook import Workbook
import pandas as pd
#importing packages


class employees:

    #function that generates an excel file of employees and their managers
    def emp_manager(self):
        try:
            #trying to connect to postgresql database
            conn = psycopg2.connect(

            database="Assignment",
            user="postgres",
            password="Ishu@123")
            cursor = conn.cursor()

            #connection established
            script = """
                    SELECT e1.empno, e1.ename, (case when mgr is not null then (select ename from emp as e2 where e1.mgr=e2.empno limit 1) else null end) as manager
                    from emp as e1 
                    """
            #query to list employee numbers, names and their managers
            cursor.execute(script)

            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)
            #storing data in dataframe

            writer = pd.ExcelWriter('ques_1.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()

            #using the data frame to generate excel file

        except Exception as e:
            #if exception thrown in try block
            logging.error("Error", e)

        finally:
            #after completion of above block,closing the connection
            if conn is not None:
                cursor.close()
                conn.close()
                #commit the connection properly.

#main method
#creating an object of employees class and calling the emp_manager method
if __name__ == '__main__':
    conn = None
    cur = None
    emp = employees()
    emp.emp_manager()
