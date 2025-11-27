import sys
if len(sys.argv) ==2:
  script_name=sys.argv[0]
  array =[name]*11
  array[10]=sys.argv[1]
else:
  array=[1,2,3,9,7,10,5]
  sum_of_elements = sum(array)
  print("sum of elements:",sum_of_elements)
  avg_of_elements = sum_of_elements/len(array)
print("average of elements :",avg_of_elements)
print("max elements :",max(array))
print("min elements :",min(array))
