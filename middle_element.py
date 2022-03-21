# Function middle element
lst = [1,2,3,4,5,6,7,8]
size_lst = len(lst)
firstnum = lst[0]
lastnum = lst[-1]
middlenum = int(lastnum / 2)
total_lst = sum(lst)
avg_lst = total_lst / size_lst
avg_middle_2 = ((middlenum) + (middlenum + 1)) / 2
def middle_element():
  if size_lst % 2 == 0:
    print("even list")
    print("list size: "+ str(size_lst))
    #print("1st element: "+ str(firstnum))
    #print("last element: "+ str(lastnum))
    #print("middle element: "+ str(middlenum))
    #print("TOTAL List: "+ str(total_lst))
    print("AVG middle two elements: "+ str(avg_middle_2))
  else:
    print("odd list")
    print("list size: "+ str(size_lst))
    print("middle element: "+ str(middlenum))
middle_element()