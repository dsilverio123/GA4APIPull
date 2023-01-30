# Google Analytics Data (GA4) API Pull to SQLite
An easy way to breakdown GA-4 API Data and to store in a SQLite database.

1. Enable the Google Analytics Data API  <a href="https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries">here!</a> 
2. Install the dependencies <a href="#anchor-name">(see below)</a>
3. With the downloaded JSON file, place into a folder where you'll be doing you're testing
4. Look into <a href="https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/credentials.json">credintials.json</a> file and look for email like: "quickstart@PROJECT-ID.iam.gserviceaccount.com", share it with your analytics property giving it admin access
5. With the  <a href="https://github.com/dsilverio123/Google-Analytics-Data-GA4-API-Pull-to-SQLite/blob/main/QuickStart.py">QuickStart.py</a> file, place your specific property view and your credentials file name into the specific places
6. Create a blank SQLite database
7. Run the program and the results will now be in the SQLLITE database

If you'd like to edit with Power Bi:

Reference this: https://apps.provingground.io/docs/tracer-v1-0-documentation/tracer-power-bi-workflow/how-to-use-sqlite-as-a-power-bi-data-source/

If you'd like to add more more metrics/dimensions, refer to this: 

Future stuff to add:

- DAG Airflow Component w/ Email Notification


<a id="anchor-name"><strong>Dependencies:</strong></a>

``` 

pip install pandas

pip install git+https://github.com/DataSolveProblems/jj_data_connector.git

```
