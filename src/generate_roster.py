import csv
import random
import string

# Define the output CSV file name
output_file = "roster.csv"

# Define the number of rows to generate
num_rows = 100

# Predefined values for certain fields
categories = ["A", "C", "T"]  # Example categories
csnp_values = ["Yes", "No"]
gender_values = ["Male", "Female"]
hospice_values = ["Yes", "No"]
aww_elig_values = ["Yes", "No"]
states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Generate random values
def random_member_id():
    return random.randint(10000, 99999)

def random_name():
    first_names = ["Ida", "Isidore", "Elfrida", "Quint", "Marianne", "Ward", "Zelda", "Annecorinne"]
    last_names = ["Brashier", "Extall", "Middiff", "Matevosian", "Gronno", "McSweeney", "Gilchrist", "Whitlow"]
    return f"{random.choice(first_names)}, {random.choice(last_names)}"

def random_dob():
    year = random.randint(1930, 2024)  # Generate realistic birth years
    month = random.randint(1, 12)
    return f"{year}{str(month).zfill(2)}"  # YYYYMM format

def random_age():
    return random.randint(65, 80)

def random_raf():
    return round(random.uniform(1.0, 2.0), 2)

def random_zip():
    return str(random.randint(10000, 99999))

def random_phone():
    return f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_address():
    street_names = ["Main St", "Washington Ave", "Crest Line St", "Dakota Hill", "Shasta Place"]
    return f"{random.randint(100,9999)} {random.choice(street_names)}"

def random_city():
    cities = ["Dallas", "San Antonio", "Los Angeles", "San Diego", "Houston", "Chicago", "Philadelphia"]
    return random.choice(cities)

# Writing to CSV
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Writing the header
    writer.writerow(["CATEGORY", "MEMBER ID", "C-SNP", "MEMBER NAME", "DOB", "AGE", "GENDER", "RAF",
                     "CY MOS w/TIN", "HOSPICE", "AWW ELIG", "CY AWV DATE", "ADDRESS", "CITY", "STATE", "ZIP", "PHONE NUMBER"])

    # Writing data rows
    for _ in range(num_rows):
        writer.writerow([
            random.choice(categories),  # CATEGORY
            random_member_id(),         # MEMBER ID
            random.choice(csnp_values), # C-SNP
            random_name(),              # MEMBER NAME
            random_dob(),               # DOB
            random_age(),               # AGE
            random.choice(gender_values), # GENDER
            random_raf(),               # RAF
            random.randint(1, 24),      # CY MOS w/TIN (assuming 1-24 months)
            random.choice(hospice_values),  # HOSPICE
            random.choice(aww_elig_values), # AWW ELIG
            random_dob(),               # CY AWV DATE (using same format as DOB)
            random_address(),           # ADDRESS
            random_city(),              # CITY
            random.choice(states),      # STATE
            random_zip(),               # ZIP
            random_phone()              # PHONE NUMBER
        ])

print(f"CSV file '{output_file}' has been generated successfully with {num_rows} rows.")
