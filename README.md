# Assignment1
Import Excel data to Mysql db by Python script
First of all Python's XLRD library is needed to extract data from excel spreadsheet in order to do so, [$ pip install xlrd]  command is easiest one
MySqlDb module is also necessary to connect to the database;following pip command can be used to download the api[pip install mysql-connector-python]
Next have to create the table that we like to use in our database by sql command as follows...

                                          CREATE TABLE Moldeddata (
                                                 Product Name varchar(255), 
                                                 Model Name varchar(255), 
                                                 Product Serial No int varchar(255), 
                                                 Group Assosiated varchar(255), 
                                                 product MRP(rs.) int,
                                                 );


After that Python script is written to import the data with aforementioned comment
