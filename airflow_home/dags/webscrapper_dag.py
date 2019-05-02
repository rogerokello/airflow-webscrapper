import datetime as dt
from bs4 import BeautifulSoup
from urllib import request
import re

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator


def scrape_from_web():
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    try:
        page = request.urlopen(url)
    except:
        print("An error occured.")

    soup = BeautifulSoup(page, 'html.parser')
    regex = re.compile('^tocsection-')
    content_lis = soup.find_all('li', attrs={'class': regex})

    content = [li.getText().split('\n')[0] for li in content_lis]

    with open('content.txt', 'w') as f:
        for i in content:
            f.write(i+"\n")

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2019, 4, 26, 12, 42, 00),
    'concurrency': 1,
    'retries': 0
}

with DAG(
        'web_scrapper',
        default_args=default_args,
        schedule_interval='*/10 * * * *',
) as dag:
    opr_info = BashOperator(task_id='information_1',
                            bash_command='echo "Pick from the"')

    opr_greet = PythonOperator(task_id='scrape_from_wiki',
                               python_callable=scrape_from_web)

    opr_sleep = BashOperator(task_id='sleep_me', bash_command='sleep 5')

opr_info >> opr_greet >> opr_sleep
