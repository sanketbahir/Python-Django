

def main():
  emp_numbers = int(input())
  emplist=[]
  print('Enter the name of emp ')
  for i in range(emp_numbers):
    value = input()
    emplist.append(value)
  print('list of employee',emplist)


if __name__=="__main__":
  main()

def main():
    num_employees = int(input("Enter the number of employees: "))
    salary_list = []
    print('Enter the salaries of the employees:')
    for i in range(num_employees):
        salary = float(input())
        salary_list.append(salary)
    print('List of employee salaries:', salary_list)

if __name__ == "__main__":
    main()




