# Automated_data_pipeline
## Data Engineering : Automated Data Pipeline on mySQL cloud database

The objective of this project is to create a data pipeline that gathers information from the internet, processes it, and stores it in a database, transitioning from a local setup to a cloud-based infrastructure. The project is divided into two main phases: Local Pipeline and Cloud Pipeline.

**Phase 1: Local Pipeline**

In this phase, the focus is on setting up a local environment for data collection and storage.

1.1. **Scrape Data from the Web**: Learn how to access and extract information from websites by downloading and parsing their HTML code using the Beautiful Soup library in Python.

1.2. **Collect Data with APIs**: Acquire data from various internet data providers using APIs. Learn how to authenticate, assemble requests, and interact with APIs using Python's requests library.

1.3. **Create a Database Model**: Define the logical structure of a relational database to store the collected data. Determine the required tables and their relationships, paving the way for efficient data storage and retrieval.

1.4. **Store Data on a Local MySQL Instance**: Set up a local MySQL database on your computer and store the collected data from both web scraping and APIs. Ensure that the connection between Python and MySQL is functional.

**Phase 2: Cloud Pipeline**

In this phase, the project transitions to a cloud-based infrastructure for improved scalability and automation.

2.1. **Set up a Cloud Database**: Utilize Amazon Web Services' (AWS) Relational Database Service (RDS) to create a cloud-hosted MySQL database. This step improves the scalability and accessibility of the database.

2.2. **Move Scripts to Lambda**: Migrate the data collection scripts from Jupyter Notebooks to AWS Lambda functions. Lambda is a cloud service that allows code execution without managing server infrastructure.

2.3. **Automate the Pipeline**: Leverage AWS CloudWatch Events or EventBridge to schedule and automate the execution of data collection scripts. This automation simplifies the process and ensures data collection occurs at specific intervals or based on triggers.

Overall, this project aims to create an efficient and automated data pipeline, initially on a local environment and later transitioning to a cloud-based setup, utilizing AWS services to enhance scalability and maintainability.

## Architecture 
- Collect Data with Web Scraping
- collect data with APIs
  ![image](https://github.com/Fabiano2415/Automated_data_pipeline/assets/101226686/c7ba0363-9314-41cc-9302-90c649bc69b6)

