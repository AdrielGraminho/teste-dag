#!/usr/bin/env python
# coding: utf-8

# In[1]:


from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator


# In[3]:


default_args = {
   'owner': 'admin',
   'depends_on_past': False,
   'start_date': datetime(2022, 9, 16),
   'retries': 0,
   }


# In[6]:


with DAG(
    'my-first-dag',
    schedule_interval=timedelta(minutes=1),
    catchup=False,
    default_args=default_args
) as dag:
    t1 = BashOperator(
        task_id='first_etl',
        bash_command="""
        echo "hello"
        """)
    t2 = BashOperator(
        task_id='second_etl',
        bash_command="""
        echo "hello 2"
        """)
    t1 >> t2

