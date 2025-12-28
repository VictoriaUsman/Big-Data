from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json
from datetime import datetime




# Define the DAG
with DAG(
    dag_id = 'Ian_Tristan_ETL_NASA_Postgres_ETL',
    start_date = datetime(2024,1,1),
    schedule = '@daily',
    catchup = False


) as dag:

    ## Step 1: Create the table if it doesn't exists
    @task
    def create_table():
        ###initialize the Postgreshook###
        postgres_hook = PostgresHook(postgres_conn_id = 'postgres_connection')

        ### SQL Query 
        create_table_query = '''
            DROP TABLE IF EXISTS apod_data;
            CREATE TABLE IF NOT EXISTS apod_data(
                id SERIAL PRIMARY KEY,
                title VARCHAR(225),
                explanation TEXT,
                url TEXT,
                date DATE,
                media_type VARCHAR(50)
            
            
            );

        '''
        #Execute the table creation query
        postgres_hook.run(create_table_query)

    ## Step 2: Extract the NASA API Data(APOD)- Astronomy Picture of the Day [Extract Pipeline]
    extract_apod = HttpOperator(
        task_id="extract_apod",
        http_conn_id="nasa_api",
        endpoint="planetary/apod?api_key=?????????",
        method="GET",
        response_filter=lambda response: response.json(),
        log_response=True,
    )




    ## Step 3: Transform the data(Pick the Information that I need to save) [Transfrom Pipeline]
    @task
    def transform_apod_data(response):
        apod_data =  {
            'title': response.get('title', ''),
            'explanation': response.get('explanation',''),
            'url': response.get('url', ''),
            'date': response.get('date',''),
            'media_type': response.get('media_type','')

        }
        return apod_data

    ## Step 4: Load the Data to Postgres SQL [Load Pipeline]
    @task
    def load_to_postgres(apod_data):
        postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')

        insert_query = '''
            INSERT INTO apod_data(
                title,
                explanation,
                url, 
                date,
                media_type
            )
            VALUES (%s, %s, %s, %s, %s);
        '''

        postgres_hook.run(insert_query, parameters=(
            apod_data['title'],
            apod_data['explanation'],
            apod_data['url'],
            apod_data['date'],
            apod_data['media_type'],
        ))


    # Execute query using the hook
       

    ## Step 5: Verify the data DBeaver



    ## Step:6: Define Task Dependencies

    #EXTRACT
    create_table() >> extract_apod   #ensure table is create before extraction
    api_response = extract_apod.output

    #TRANSFORM
    transformed_data = transform_apod_data(api_response)

    #LOAD
    load_to_postgres(transformed_data)