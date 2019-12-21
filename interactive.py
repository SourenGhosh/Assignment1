import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook(" beginner_assignment01.xls")
sheet = book.sheet_by_name("source")

# Establish a MySQL connection
database = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "mysqlPython")

# Get the cursor, which is used to traverse the database, line by line
cursor = database.cursor()

# Create the INSERT INTO sql query
query = """INSERT INTO orders (Product Name, Model Name, Product Serial No, Group Assosiated, product MRP(rs.)) VALUES (%s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
for r in range(1, sheet.nrows):
		Product	Name = sheet.cell(r,).value
		Model Name = sheet.cell(r,1).value
		Product Serial No = sheet.cell(r,2).value
		Group Assosiated = sheet.cell(r,3).value
		product MRP(rs.) = sheet.cell(r,4).value
		# Assign values from each row
		values = (Product Name, Model Name, Product Serial No, Group Assosiated, product MRP(rs.))

		# Execute sql Query
		cursor.execute(query, values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()

# Print results
print ""
print "All Done!"
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print "I just imported " %2B columns %2B " columns and " %2B rows %2B " rows to MySQL!"
