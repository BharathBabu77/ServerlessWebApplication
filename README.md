# ServerlessWebApplication Using AWS Lambda

This is a serverless web application built using various AWS services including S3, CloudFront, Lambda, IAM Role, DynamoDB, and API Gateway. It allows you to store and retrieve employee profiles in a DynamoDB table through a RESTful API.

Services Used

S3: Used to store the front-end code (profile.html, scripts.js).

CloudFront: Used as a content delivery network (CDN) to distribute the web application globally.

Lambda: Used to create serverless functions for retrieving and inserting employee data into DynamoDB.

IAM Role: Used to define the necessary permissions for the Lambda functions to access DynamoDB.

DynamoDB: Used as the NoSQL database to store employee profiles.

API Gateway: Used to create a RESTful API for accessing the Lambda functions.

Steps to Set Up the Application

Create an S3 bucket to store the front-end code (profile.html, scripts.js).

Create a CloudFront distribution and copy the generated policy to the S3 bucket policy.

Create an IAM Role with full access to DynamoDB.

Create a DynamoDB table (employeeProfile) with the empId as the partition key.

Create a Lambda function (getEmployee) to retrieve employee details from the DynamoDB table.

Create a Lambda function (insertEmployeeData) to insert employee data into the DynamoDB table.

Create a REST API (Employee) using API Gateway.

Create a GET method and link it to the getEmployee Lambda function.

Create a POST method and link it to the insertEmployeeData Lambda function.

Deploy the API Gateway and copy the generated link into the scripts.js file, then upload it to the S3 bucket.

Enable Cross-Origin Resource Sharing (CORS) to allow the web application to access the API Gateway.

Execution

Copy the CloudFront distribution domain name and paste it into your browser.

Enter the employee details in the web application and click "Save Profile". This will trigger the insertEmployeeData Lambda function and store the details in DynamoDB.

Click on "View All Employee Profiles" to fetch and list the saved profiles from DynamoDB. This will trigger the getEmployee Lambda function.
