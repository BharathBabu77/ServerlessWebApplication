# Serverless Web Application Using AWS Lambda

Services used:S3,Cloud Front,Lambda,IAM Role,Dynamo DB,API Gateway

Steps:
Create an S3 bucket to store the front end code(profile.html, scripts.js)
Create a cloudfront distribution and copy the policy generated to the S3 bucket policy
Create an IAM role which has DynamoDB full access
Create a Dynamo DB table (employeeProfile) with partition as empId
Create a lambda function (getEmployee) to get the details stored in Dynamo DB table
Create a lambda function (insertEmployeeData) to insert the data into Dynamo DB table
Create a Rest API(Emloyee) using API Gateway
Create GET method and link getEmployee lambda function
Create POST method and link insertEmployeeData lambda function
Deploy API Gateway and copy the link generated into scripts.js file and upload in to S3
Enable CORS
 
Execution:
Copy the cloud front distribution domain name and paste in browser
Enter the Employee details and click on save profile
The details will be automatically stored into Dynamo DB as lambda function (insertEmployeeData) will be triggered
Click on view all employee profiles ,the saved profiles will be fetched from Dynamo DB and listed below
lambda function (getEmployee) will be triggered in this step 


