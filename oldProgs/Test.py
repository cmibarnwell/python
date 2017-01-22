def pascal(n):
   row = 1
   k = 0
   for x in range(n):
      print(row)
      for i in range(row):
          row=i
   
pascal(10)
