import boto3
import csv


# Initialize a function called iam_policy

def iam_policy():
    # Initialize the IAM Client]
    client = boto3.client('iam')
    # Get all policies in your AWS account
    all_policies = client.list_policies()['Policies']


    # Create a CSV call policies.csv, set it to write mode, format column names within quotations to appear on a newline for readability

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

# Call the function to run the program
iam_policy()


# NB..For boto3 to get your access credentials quickly and in a safe manner just run aws configure first and set the configurations asked

