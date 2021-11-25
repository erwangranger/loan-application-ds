import pandas as pd

csv_data_file_url="https://gist.githubusercontent.com/erwangranger/c1534647ecd6efc6188a92d69657f3bc/raw/dcdfb27ef1c23c37cde56c2f09f19023d0809e12/loans.csv"

raw_loans_data = pd.read_csv(csv_data_file_url)
trimmed_loans_data = raw_loans_data[['Loan_ID','LoanAmount','Credit_History','Loan_Status']]

print ("data has been imported")
print ("here are the dataframes available to you\n")

%whos DataFrame