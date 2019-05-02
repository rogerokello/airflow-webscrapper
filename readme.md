# This shows a simple ETL pipeline created using Apache airflow 

## Introduction
Airflow is a platform to programmatically author, schedule and monitor workflows. An ETL pipeline is just an example of such a workflow. Apache airflow may be used for other processes such as:
- Monitoring Cron jobs
- transferring data from one place to other.
- Automating your DevOps operations.
- Periodically fetching data from websites and update the database for your awesome price comparison system.
- Data processing for recommendation based systems.
- Machine Learning Pipelines.

## Installation on Mac
1. Clone the application into any location
2. cd into project-one
3. Run the command `export AIRFLOW_HOME='pwd' airflow_home` to set the default home for airflow
4. Set up the virtual-environment using `python3 -m venv venv`
5. Activate the virtual environment using `source venv/bin/activate`
6. Install requirements using `pip3 install -r requirements.txt`
7. cd into airflow_home by running `cd airflow_home`
8. Run the command `airflow initdb` from with in the airflow_home directory to create the airflow configuration and unit tests
9. Run the command `airflow scheduler --subdir "path/to/dag/folder"` while substituting the path to the dag folder with an absolute path to your dag folder.
10. Duplicate the above terminal in step 9. and activate the virtual environment.
11. Run the command `airflow webserver`.
10. The above command starts the webserver and starts the scheduler that will execute the dags
11. Visit the url http://0.0.0.0:8080/
12. Look for the dag named `web_scrapper`, turn it on and trigger it.
13. A file named `content.txt` should be created from in the airflow_home folder with some content.
