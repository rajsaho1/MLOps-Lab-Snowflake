import snowflake.connector
from snowflake.snowpark import functions
from snowflake.snowpark.types import *
from snowflake.snowpark.functions import udf
from snowflake.snowpark.session import Session
from snowflake.snowpark.functions import sproc
from snowflake.snowpark.functions import call_udf, array_construct, col

connection_params = dict(user='ramsagar',

                         password='Tippu@1522',

                         account="zq78716.europe-west2.gcp",

                         warehouse="REFRACT",

                         database="LOAN_DEFAULT",

                         schema='INFORMATION_SCHEMA',

                         role='ACCOUNTADMIN')


session = Session.builder.configs(connection_params).create()

print('Successfully executed')

