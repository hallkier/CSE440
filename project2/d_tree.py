def DT(filename):

   with open(filename, 'r') as f:
       num_inst = 0
       data_bool = false
       for line in f:
           if data_bool == true:
               num_inst = num_inst + 1
            if line == ("@data"):
                data_bool = true

        print ("Number of instances: ", num_inst)


DT(set1.data)







