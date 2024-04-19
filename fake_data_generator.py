from faker import Faker
import random
import csv

fake = Faker()

#--------------------- writting a test csv with 500 rows

#a function to generate random sex choices
def generate_sex():
    return random.choice(['F', 'M'])

#a function to generate random education year
def generate_education_year():
    return random.randint(1, 5)

#test CSV data (500 data points)
test_data = []

for _ in range(500):
    row = [
        fake.first_name(),
        fake.last_name(),
        generate_sex(),
        fake.email(),
        fake.phone_number(),
        fake.city(),
        generate_education_year(),
        fake.name(),
        fake.date_of_birth(),
        fake.job()
    ]
    test_data.append(row)

#header
header = ['First Name', 'Last Name', 'Sex', 'Email', 'Phone Number', 'City', 'Current Ed Year', 'Primary Supervisor', 'Date of Birth', 'Job Title']
test_data.insert(0, header)

#writting data to CSV file
with open('test_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(test_data)

#confirmation
print("CSV data has been generated and saved as 'test_data.csv'.")