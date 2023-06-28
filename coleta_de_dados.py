import requests
import psycopg2
import schedule
import time

def extrair_dados(url,conn,cursor):
    response = requests.get(url)
    data = response.json()
    for item in data:
        cursor.execute(" INSERT INTO tabela (column1, column2) VALUES (%s %s)",(item['column1'], item['column2']))
    conn.commit()

def timer_extract():
    conn = psycopg2.connect(
        host=
        database=
        user=
        password=
    )
    cursor = conn.cursor()

    sites=[]

    for site in sites:
        extrair_dados(site,conn,cursor)
        cursor.close()
        conn.close()
        
schedule.every().hour.do(timer_extract)

while True:
        schedule.run_pending()
        time.sleep(1)