import csv

def calculate_total_revenue(csv_file):
    total_revenue = 0
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader) # skip the header row
        for row in reader:
            sale_date = row[0]
            sale_value = float(row[1])
            if '2022-04' <= sale_date <= '2023-03':
                total_revenue += sale_value
    return total_revenue

# Test the function with the provided CSV file
csv_file = 'sales_data.csv'
total_revenue = calculate_total_revenue(csv_file)
print(f'Total revenue for FY 2023: ${total_revenue:.2f}')
