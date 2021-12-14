import streamlit as st
import mysql.connector


class db_operations():
    def __init__(self): # constructor with connection path to db
        self.connection = mysql.connector.connect(
        **st.secrets["mysql"]
        )
        self.cursor = self.connection.cursor()
        print("connection made..")

    def bulk_insert(self,query,records):
        self.cursor.executemany(query,records)
        self.connection.commit()
        print("query executed..")

    def run_query(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def single_attribute(self,query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        #results = [i[0] for i in results]
        #results.remove(None) -- throws errors
        return results
