# import pandas as pd

# # read the CSV file
# df = pd.read_csv("20k.csv")

# # count the number of rows in the DataFrame
# row_count = len(df.index)

# # print the number of rows
# print("Number of rows:", row_count + 1)

### ======== csv ===============

# import pandas as pd

# # read the CSV file
# df = pd.read_csv("tt.csv")

# # specify the header name
# header_name = "Submitted Credits"

# # calculate the sum of the row of that header
# header_sum = df[header_name].sum()

# # print the sum
# print("Sum of", header_name, ":", header_sum)

### ======== xlsx ===============

# import pandas as pd

# df = pd.read_excel("tt.xlsx")

# header_name = "Submitted Credits"

# header_sum = df[header_name].sum()

# print("Sum of", header_name, ":", header_sum)


### ======== xlsx ===============

# import pandas as pd

# # read the XLSX file
# df = pd.read_excel("file.xlsx")

# # specify the header name
# header_name = "Submitted Credits"

# # get the values in the row of that header
# header_values = df[header_name].tolist()

# # count the data in the row of that header one by one using a loop
# count = 0
# for value in header_values:
#     count += 1

# # print the count
# print("Count of", header_name, ":", count)



# []
import re
Input = input("Enter password : ")
pattern = "^[0-9,a-z,A-Z]{6,}$"
Pass = re.match(pattern , Input)

if Pass:
    print("Validate")
else:
    print("Not valid password")