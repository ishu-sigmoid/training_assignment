import psycopg2
import logging
from openpyxl.workbook import Workbook
import pandas as pd
# importing packages


class Compensation:

    # function to list the Total compensation given till his/her last date or till now and store it in a excel file
    def total_compensation(self):
        try:
            # trying to connect to postgresql database
            conn = psycopg2.connect(

                database="Assignment",
                user="postgres",
                password="Ishu@123")
            #confidential information like password should not be shared on open source code; rather use environment variables or config file.
            cursor = conn.cursor()
            # connection established
            script = """
                     select emp.ename, emp.empno, dept.dname, (case when enddate is not null then ((enddate-startdate+1)/30)*(jobhist.sal) else ((current_date-startdate+1)/30)*(jobhist.sal) end)as Total_Compensation,
                    (case when enddate is not null then ((enddate-startdate+1)/30) else ((current_date-startdate+1)/30) end)as Months_Spent from jobhist, dept, emp 
                    where jobhist.deptno=dept.deptno and jobhist.empno=emp.empno
                    """
            # query to list the Total compensation given till his/her last date or till now and store it in a excel file
            cursor.execute(script)

            columns = [desc[0] for desc in cursor.description]
            data = cursor.fetchall()
            df = pd.DataFrame(list(data), columns=columns)
            # storing data in dataframe
            writer = pd.ExcelWriter('ques_2.xlsx')
            df.to_excel(writer, sheet_name='bar')
            writer.save()
            # using the data frame to generate excel file

        except Exception as e:
            # if exception thrown in try block
            logging.error("Error", e)

        finally:
            # after completion of above block,closing the connection
            if conn is not None:
                cursor.close()
                conn.close()


# main method
# creating an object of Compensation class and calling the total_compensation method
if __name__ == '__main__':
    conn = None
    cur = None
    salary = Compensation()
    salary.total_compensation()
