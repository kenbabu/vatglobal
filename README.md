
# Vatglobal Developer Assignment

##  Task Summary

Create a Django based API that uploads a CSV and retrieves the contents of the CSV using REST API calls.

## Installed Apps
Please ensure that the following apps are installed though not part of the original test would make running the applicaion easier
1. ``` pip install django-filter ``` for filtering records in django rest. Please follow [installation instructions](https://django-filter.readthedocs.io/en/stable/guide/install.html)
2. ``` pip install django_crispy_forms ```
3. Most importantly ensure that the djangorestframework is installed `pip install djangorestframework` NB: I could have included all this in a  `requirements.txt` but I used a `conda environment` 
4. on my machine hence the requirements file would've had too many contents that are not related to this assignment.
`

## Access the software
1. Clone the repository from github ```git clone https://github.com/kenbabu/vatglobal.git ```
2. Create the databases by navigating to the project directory and running ``` python manage.py makemigrations ``` followed by ``` python manage.py migrate ```
3. From the project directory execute ```python manage.py runserver```
4. Click the ```Upload CSV ``` to access the file Upload Page
5. Locate the CSV file by clicking on the `Choose file` button
6. Click Upload
7. The CSV is read and its contents are validated, and automatically uploaded into the `Transaction` model.



## Completed tasks
- File can be uploaded and loaded into Django model
- Records can be queried based on ``` country ```, ```trans_date ``` and ``` currency ```


Create a Django based API using the Django REST Framework to allow a user to upload a data file for processing, and to retrieve a list of processed rows. 

The application should expose the two following endpoints: 
1. `http://localhost:8000/api/retrieveRows/` for retrieving rows. I changed the api urls slightly to make them intuitive b
2.  I also filter the dates based on the format in which they are stored in the database 'YYYY-MM-DD'

## Additional tasks
These are tasks that were not part of the test but I thought necessary to build to help me with my dev work
1. Django management command for clearing the database
2. Basic frontend for running the code

## Scalability 
I'd handle scalability in various ways. However, for this task I'll mention three ways two of which are implemented in the solution.
1. Avoid unnecessary queries that ties up the database. For example in this test I didn't save the records one by one as I read them from the CSV but rather aggregated them in a list then using `bulk_create` transaction query to create multiple objects.
2. I'd also use management commands that can be run behind the scenes to improve user experience by not subjecting the user to long waits as data is getting uploaded. As mentioned above I created an example of a management command for clearing the database.
3. Another alternative is to paralellize the code by utilising multiple cores of a machine, using multiple threads or writing code that can be run on a cluster machine if such a facility is available. 






