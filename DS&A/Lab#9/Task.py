import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Ali', 'Sara', 'Ahmed', 'Fatima', 'Hassan'],
    'Age': [24, 22, 21, 23, 25],
    'Department': ['CS', 'AI', 'CS', 'SE', 'AI'],
    'Marks': [85, 90, 88, 92, 78]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# View first few records
print("\nHead:")
print(df.head())

# Basic statistics
print("\nDescribe:")
print(df.describe())

# Selecting a column
print("\nMarks Column:")
print(df['Marks'])

# Filtering
print("\nStudents with marks > 85:")
print(df[df['Marks'] > 85])

# Sorting
print("\nSorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))
