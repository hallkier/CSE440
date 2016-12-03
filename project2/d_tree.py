def DT(filename):

   with open(filename, 'r') as f:
       num_inst = 0
       data_bool = false
       for line in f:
           if line == ("@data"):
                data_bool = true

           if data_bool == true:
               num_inst = num_inst + 1

        print ("Number of instances: ", num_inst)


DT(set1.data)







