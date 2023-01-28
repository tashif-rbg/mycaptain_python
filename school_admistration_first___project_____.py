# basic student administration tool 
import csv
def write_info_csv(info_list):
    with open('student_info_csv','a',newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()== 0:
            writer.writerow(['name', 'age', 'contact_info','e mail'])

        writer.writerow(info_list)

if __name__ == '__main__':
   condition = True
   student_no = 1
   while condition:
     student_info = input("Enter the srudent 1 {} info in follwing formal (name , age , contact_no , E mail id :".format(student_no))
     print("Entered info :"+student_info)

     student_info_list = student_info.split(' ')

     print("\nThe entered info is \nname : {} \nage : {} \ncontact_no : {} \nE mail : {} "
    .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

     check = input("is entered info correct (yes/no) :")

     write_info_csv(student_info_list)

     condition_check = input("Enter (yes/no) if you want to enter more info :")
     if condition_check == 'yes':
        condition = True
        student_no = student_no+1
     elif condition_check == 'no':
        condition = False
     elif check == "no":
        print("\n please re-enter the info :")
