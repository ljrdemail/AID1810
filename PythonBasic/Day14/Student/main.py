from PythonBasic.Day14.Student.menu import show_menue
from PythonBasic.Day14.Student.student_info import *


def main():
    infos = []
    while True:

        show_menue()
        s = input("请选择: ")
        if s == '1':

             infos += input_student()



        elif s == '2':

            output_student(infos)
        elif s == '3':
            str = input("请输入要删除的姓名！")

            del_student(str, infos)
        elif s == '4':
            str = input("请输入要修改的姓名！")

            update_student(str, infos)
        elif s == '5':

            sor_by_score_desc(infos)
        elif s == '6':

            sor_by_score_asc(infos)
        elif s == '7':

            sor_by_age_desc(infos)
        elif s == '8':

            sor_by_age_asc(infos)
        elif s == 'q':
            break
        else:
            print("你输入的菜单不存在，请重新输入！")


main()
