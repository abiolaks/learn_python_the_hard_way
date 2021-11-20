# The programs aim to allow user enter an amount : tolal salary 
# The display the what is left as it is been spent on expenses
# the expenses is display and what is left is returned



# displaying a nice header
print()
print("**************___________***************")
print()
# displaying the text below
print("...... Building A Salary Expenditure App ......")
print()
# collecting the salary earn from user
monthly_salary = float(input("****** Please Enter Salary For This MOnth ****** : "))

# user entering the amount needed currently to spend on expenses

expense = float(input("****** How much are you spending now? ******: "))

# what are you spending the money on 
purpose = input("****** what are you spending it on****** : ")
# mathematical operation to compute what is left after expense is made from salary
balance = monthly_salary - expense

print()
# displaying the output and formattin text using f string
print(f"What is left after after spending {expense} for {purpose} is {balance}. Do ensure to spend the rest wisely")

# displaying a close header
print()
print("******That is it for now Enjoy Your Day******")
