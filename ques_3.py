import psycopg2
import xlrd
import openpyxl
import os
import pandas as pd
import logging
#importing packages

#class to create a table and upload data of "ques_2.xlsx" to postgres databse
class Employees:

    #function to create table and upload data
    def upload_data(self):
        try:
            df= pd.read_excel("question2.xlsx")
            #creating dataframe

            database = psycopg2.connect (database = "sql", user="postgres", password="rahul")#, host="localhost", port="5432")
            #connection established

            cursor = database.cursor()
            query1="""
            CREATE TABLE Compensation_Employee (
            emp_name varchar(10) ,
            emp_no integer PRIMARY KEY,
            dept_name VARCHAR ( 50 ) ,
            Total_Compensation numeric,
            Months_Spent numeric
     );
    """
            #creating the table


            query = """INSERT INTO Compensatation_Employee (emp_name, emp_no, dept_name, Total_Compensation, Months_Spent) VALUES (%s, %s, %s, %s, %s)"""
            #Inserting the values in created table

            for r in range(1,len(df)):

                emp_name=df['ename'][r]
                emp_no=df['empno'][r]
                dept_name=df['dname'][r]
                Total_Compensation = df['total_compensation'][r]
                Months_Spent=df['months_spent'][r]

            values = (emp_name, emp_no, dept_name, Total_Compensation, Months_Spent)
            #storing values in tuple
        #values.to_sql(openpyxl, 'Compensation', if_exists='append', index=False)
            cursor.execute(query1)
            cursor.execute(query, values)
            #executing the queries


    #print(df)

        except Exception as e:
            # if exception thrown in try block
            logging.error("Error", e)

        finally:
            # after completion of above block,closing the connection and commiting to the database
            cursor.close()
            database.commit


# main method
# creating an object of Employees class and calling upload_data method
if __name__ == '__main__':
    conn = None
    cur = None
    emp = Employees()
    emp.upload_data()