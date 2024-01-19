print ("Running the query please wait")
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import mysql.connector
import google.generativeai as genai

##Configure API Key

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide sql query as response 

def get_gemini_response(question, prompt):

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

##Function to retrieve query from the sql database

def read_sql_query(sql, db):
    # Replace the following with your MySQL database credentials
    host = "localhost"
    user = "root"
    database = db

    # Retrieve the database password from the environment variable
    password = os.environ.get("SQL_LOCAL_PASSWORD")

    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        if connection.is_connected():
            print("Connected to MySQL database")


            # Create a cursor to execute SQL queries
            cursor = connection.cursor()
            
            # Query to the database
            cursor.execute(sql)

            # Fetch column names if available
            columns = [column[0] for column in cursor.description]
            print("Column Names:", columns)

            # Fetch all rows
            rows = cursor.fetchall()

            # Display the results
            for row in rows:
                print(row)
                st.write(row)

            return rows

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the database connection in the finally block
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")

##Define the prompt

prompt = [
        """
          You are an expert in converting English questions to MySQL query.
          The name of the table is customers
          The Mysql table has the following columns: CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country
          I should be able to directly copy paste the output that you provide. So do not include any extra words or special characters which are not necessary for the query.
          Do not include ''' or sql in the response
          use trim function before every variable. Eg. instead of where country = 'germany', use where trim(country) = 'germany'

          """
          
          ]

## Streamlit App

st.set_page_config(page_title = "Use natural language to query SQL Database")
st.header("App to Retrieve SQL Data using Natural Language")

question = st.text_input("Input: ", key='input')

submit = st.button("Ask the question")

#If submit button is clicked

if submit:
    llm_response = get_gemini_response(question, prompt)
    print (llm_response)
    st.header("The LLM generated query is: ")
    st.write(llm_response)
    st.subheader("The response form DB is: ")
    read_sql_query(llm_response, "generative_sql")

