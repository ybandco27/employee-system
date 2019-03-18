# employee-system
An employee management system built in Python that manages data including payroll, salary range and names

The attributes of an employee are name, payroll number, job title and salary. 

In the main body of the program, the user is prompted for a filename and the program will attempt to open the file whose name is supplied. If the file cannot be opened an error message will be output and the program will terminate; otherwise the program will read each line from the file and supply it to the employee tuple-creation function, storing the tuples returned by this function in a list.

After the data has been input the program will display details of all the employees in the list in a neat table, then enter a loop in which the user is given the option of requesting the display of (a) full details of (i) the employee with a given payroll number or (ii) all employees with a salary in a particular range (e.g. 20000 to 30000) or (b) the first and last names of all employees with a specified job title using the format Bartholomew Simpson (other names, when they exist, will not be output) or quitting the program. 

The user is then asked to supply the job title, payroll number or lower and upper bounds of the salary range (as appropriate), the list is then searched and the appropriate output displayed (using the function written earlier when full details are required). The salary output is sorted numerically in ascending order of salary. Appropriate messages will be displayed if a search produces no results. The user will be told what has to be typed in order to select each option in order to allow quick testing of the program.   

The function search_employees() takes a string argument, and creates and returns a tuple containing details of the employee specified by the string. The string should be assumed to have the format 

```
12345 25000 Consultant Bartholomew Homer Simpson 
```

The first three items in the line are the payroll number, salary and job title and the rest of the line is the name. There are no spaces in the job title but there are spaces in the name. The tuple contains exactly 5 items: the payroll number, salary, job title, surname and other names. The other names are stored as a single string; the surname is the last name in the input line so in the example above the surname is Simpson and the other names are Bartholomew Homer.

The function print_employees() prints the details of an employee on a single output line. It should take a tuple as its argument and print the details in fixed-width fields using a layout such as

```
Simpson, Bartholomew Homer     12345 Consultant      £25000
```

The name is displayed in a single fixed-width field using the format above. No employee name will contain more than 30 characters when displayed in this format, no job title will contain more than 15 characters, payroll numbers will contain at most 5 digits and all salaries are integers less than 1,000,000. 
