import csv

def read_data(): # Reads the CSV file and adds the data to a Python list of dictionaries
    data = []

    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)

    return data

def sales_data(): # Returns a list of sales figures only
    data = read_data()

    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    return sales

def total_sales(): # Sums sales figures
    data = sales_data()
    total = sum(data)
    print(f'Total sales: £{total}')

    return total

def min_sales(): # Finds month with lowest sales
    data = read_data()
    sales = sales_data()
    lowest_sales = min(sales)
    index = sales.index(lowest_sales)
    print(f"Month and year of lowest sales: {data[index]["month"]} {data[index]["year"]}")

def max_sales(): # Finds month with highest sales
    data = read_data()
    sales = sales_data()
    highest_sales = max(sales)
    index = sales.index(highest_sales)
    print(f"Month and year of highest sales: {data[index]["month"]} {data[index]["year"]}")

def avg_sales(): # Calculates average monthly sales
    sales = sales_data()
    total = int(total_sales())
    print(f"Average monthly sales = £{total / len(sales)}")

def monthly_changes(): # Calculates percentage change in sales month-by-month
    data = read_data()
    sales = sales_data()
    percentage_changes = [] # Creates a list of the percentage changes
    for i in range(1, len(sales)):
        old_value = sales[i - 1]
        new_value = sales[i]
        percentage_change = ((new_value - old_value) / old_value) * 100
        percentage_changes.append(round(percentage_change, 2))
    print("Percentage change month-by-month:") # Prints the changes in a readable format
    for y in range(1, len(data)):
        print(f"to {data[y]["month"]} {data[y]["year"]}: {percentage_changes[y-1]}%")


total_sales()
min_sales()
max_sales()
avg_sales()
monthly_changes()