# write a python program to get the area of the rectangle by using function methods =>
# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# def get_area_of_rectangle(len_of_rectan , wid_of_rectan) :
#     print("the length of the rectangle is = "+str(len_of_rectan))
#     print("the width of the rectangle is = "+str(wid_of_rectan))
#     area_of_rectangle = len_of_rectan * wid_of_rectan 
#     print("the area of the rectangle is = "+str(area_of_rectangle)+" , because the length of the rectangle is = "+str(len_of_rectan)+" , and the width of the rectangle is = "        +str(wid_of_rectan))
# get_area_of_rectangle(length_of_rectangle , width_of_rectangle)

# length_of_rectangle = float(input("please enter the length of the rectangle is = "))
# width_of_rectangle = float(input("please enter the width of the rectangle is = "))
# def get_area_of_rectangle(len_of_rectan , wid_of_rectan) :
#     print("the length of the rectangle is = "+str(len_of_rectan))
#     print("the width of the rectangle is = "+str(wid_of_rectan))
#     if((len_of_rectan > 0) and (wid_of_rectan > 0)) :
#         area_of_rectangle = len_of_rectan * wid_of_rectan 
#         print("the area of the rectangle is = "+str(area_of_rectangle)+" , because the length of the rectangle is = "+str(len_of_rectan)+" , and the width of the rectangle is = "+str(wid_of_rectan))
#     else :
#         print("there is no area of the rectangle , because the length of the rectangle is = "+str(len_of_rectan)+" , and the width of the rectangle is = "+str(wid_of_rectan))
# get_area_of_rectangle(length_of_rectangle , width_of_rectangle)

def get_area_of_rectangle(len_of_rectan , wid_of_rectan) :
    print("the length of the rectangle is = "+str(len_of_rectan))
    print("the width of the rectangle is = "+str(wid_of_rectan))
    if((len_of_rectan > 0) and (wid_of_rectan)) :
        area_of_rectangle = len_of_rectan * wid_of_rectan 
        return("the area of the rectangle is = "+str(area_of_rectangle)+" because the width of the rectangle is = "+str(wid_of_rectan)+" , and the length of the rectangle is = "+str(len_of_rectan))
    else :
        return("there is no area of the rectangle because the width of the rectangle is = "+str(wid_of_rectan)+" , and the length of the rectangle is = "+str(len_of_rectan))
length_of_rectangle = float(input("please enter the length of the rectangle is = "))
width_of_rectangle = float(input("please enter the width of the rectangle is = "))
area_of_rectan = get_area_of_rectangle(length_of_rectangle , width_of_rectangle)
print(area_of_rectan)