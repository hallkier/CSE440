def DT(filename):
   num_inst = 0
   data_bool = False
   with open(filename, 'r') as f:
      for line in f:

         #Count number of instances
         if data_bool == True:
            num_inst = num_inst + 1
         if line[0:5] == "@data":
            data_bool = True

      print("Number of instances: ", num_inst)


#input_file = input("Please enter file name: ")

DT("set1.data")







