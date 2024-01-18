# Streamlit SQL Query Generator

![image](https://github.com/ALTI-PRO/LLM-SQL-Query/assets/64363023/42351e0c-a2bf-4d4f-b4a1-8d0308282408)
![image](https://github.com/ALTI-PRO/LLM-SQL-Query/assets/64363023/870fd1cd-8024-4685-b1e8-a69f865d27fb)
![image](https://github.com/ALTI-PRO/LLM-SQL-Query/assets/64363023/7d1443db-b1a8-4f2d-8477-8b6388a999fe)


## Overview

This repository contains a Streamlit web application that allows users to generate SQL queries using natural language. The application utilizes the Google Gemini language model to convert English questions into SQL queries and retrieves data from a MySQL database.

## Features

- **Natural Language Processing:** Leverage the power of Google Gemini to understand and convert English questions to SQL queries.
- **MySQL Integration:** Connect to a MySQL database to execute generated SQL queries and retrieve data.
- **Streamlit UI:** Provide a user-friendly interface for interacting with the application.
- **Trim Function Usage:** Automatically apply the trim function to variables in generated queries for improved accuracy.

## Usage

1. Install the necessary dependencies by running `pipenv install`.
2. Set up your MySQL database and configure the connection details in the code.
3. Obtain a Google API key and set it as an environment variable (`GOOGLE_API_KEY`).
4. Run the Streamlit app using `streamlit run app.py`.
5. Input your English question, click "Ask the question," and view the generated SQL query and database response.

## Acknowledgments

- This project is powered by the Google Gemini language model.
- Special thanks to the Streamlit and MySQL communities for their support.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
