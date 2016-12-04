def DT(filename):

   with open(filename, 'r') as f:
       num_inst = 0
       data_bool = False
       for line in f:
           if line == ("@data"):
                data_bool = True

           if data_bool == True:
               num_inst = num_inst + 1
       print ("Number of instances: ", num_inst)


DT("set1.data")







