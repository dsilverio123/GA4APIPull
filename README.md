# Google Analytics Data (GA4) API Pull to SQLite
<p align="center">
  
![alt text](https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/Add%20a%20heading%20(640%20%C3%97%20320%20px).png)
  
</p>
<strong>Goal:</strong>

In this repo I want to give marketers, organizations, and businesses easy access to their GA-4 API data and give them the ability to connecting it to a database as well as creating CSV and Excel files. 

<strong>Instructions:</strong>

1. Install the dependencies <a href="#anchor-name">(see below)</a>
2. Enable the Google Analytics Data API  <a href="https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries">here!</a>
3. Rename it to "credentials.json," it will be something along the lines of "1234141.json" 
4. With the downloaded JSON file, place into a folder where you'll be doing you're testing
5. Look inside <a href="https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/credentials.json">credentials.json</a> file with notepad and look for email like: "quickstart@PROJECT-ID.iam.gserviceaccount.com", share it with your analytics property giving it admin access
6. With the  <a href="https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/QuickStart.py">QuickStart.py</a> file, place your specific property view (your GA4 view ID) and your credentials file name into the specific place.
7. Create a blank SQLite database and name it to you're likeing and save.
8. Update the <a href="https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/QuickStart.py">QuickStart.py</a> file to also have your directory location of the database you created.
9. Run the program and the results will now be in the SQLITE database, the excel spreadsheet, and the csv.

*If you'd like to view the data with Power Bi:*

Reference this: https://apps.provingground.io/docs/tracer-v1-0-documentation/tracer-power-bi-workflow/how-to-use-sqlite-as-a-power-bi-data-source/

*If you'd like to add more more metrics/dimensions:*

Reference this: https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema

<strong>Future stuff to add:</strong>

- DAG Airflow Component w/ Email Notification
- Connectors to other databases (SQL Server, PostGreSQL, MySQL)

<a id="anchor-name"><strong>Dependencies:</strong></a>

``` 
pip install git+https://github.com/googleapis/google-api-python-client
pip install pandas
pip install git+https://github.com/DataSolveProblems/jj_data_connector.git
```
