# Create a Script that iterates through a dictionary of IAM policies to create a CSV file
[link to aws.py]("aws.py")

## Requirements 
- Install pip3 with sudo apt install python3-pip
- Install unzip
- pip install boto3 module
- AWS CLI
- CSV Module
  
## Let us begin!

- Started the program by importing all necessary modules

```python

import boto3 #Boto3 is a module created to allow one to interact with aws services,processes,resources etc using python code
import csv
```

- Initialized a function

```python

def iam_policy():
````
- Initialize the IAM client:

```python
client = boto3.client('iam')
```
Note well: One can set AWS credentials and parameters in the parentheses, but it is not the safe route. Then how was I able to access my credentials?
The answer is revealed below.

- Get all policies in your AWS Account.This info is stored as Dictionary objects. To know the object names used in the dictionary, I searched client.list_policies in the search bar
  
```python
    all_policies = client.list_policies()
```

<img width="736" alt="Screenshot 2023-10-21 at 4 15 56 AM" src="https://github.com/NMonKLabs77/aws_policies-script/assets/139259756/6633bc18-9373-408d-86c4-da594fbe9054">

- Iterate through the objects in the response dictionary with a for loop
  
```python
 for policies in all_policies:
        print(f"Policy Name: {policies['PolicyName']}")
```
- From the results of the iteration create a csv file that will write the Policy Name, Policy Id, and Arn
```python
  # Define headers and csv file name,store in variables for later use
    csv_filename = "policies.csv"
    headers = ['PolicyName', 'PolicyId', 'Arn']
   
   # syntax for creating csv file below:
   # with open(<csv file variable>, mode, pass whatever parameters you like) as <variable for file>:
      # <variable to store writer method result> = csv.writer(<variable for file set previously>)
      # <variable for previously set writer method>.writerow(headers)  #nb this sets the row names
      # for loop iteration to iterate through the dictionary stored in the Iam policies
        # in a variable store the mapping of the headers to the dictionary objects 
        # use writerow(row)to write your rows to csv file

    with open(csv_filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

        for policy in all_policies:
            row = [policy["PolicyName"], policy["PolicyId"], policy["Arn"]]
            writer.writerow(row)
    
    # It is good practice to let a user know that the program or goal has been acquired successfully by printing a statement

    print("Your{csv_filename} has been successfully created!")
```

- Run the function
  
```python
iam_policy()
```

Upon running the script I received a much expected error:<br>


<img width="849" alt="Screenshot 2023-10-21 at 4 27 46 AM" src="https://github.com/NMonKLabs77/aws_policies-script/assets/139259756/581370ec-a0a4-44e0-aca0-3a7c3614837c"><br>



To figure out the easiest and safest way to use my AWS credentials, which means "Not hardcoding my AWS Credentials", ChatGPT gave me 2 options
1) In the ec2 terminal if you have AWS CLI installed type ``` aws configure ``` and place in the credentials asked. By using this method boto3 module would automatically access my credentials.
2) The use of OS module ``environ`` in a different file to store my AWS credentials and store it in a variable to be used in my running script
   

The easiest and safest method was to use the ```aws configure``` method.

## Results

<img width="967" alt="Screenshot 2023-10-21 at 4 36 06 AM" src="https://github.com/NMonKLabs77/aws_policies-script/assets/139259756/027ad2d6-9b64-4132-b8e5-e3d5e40b1434">



