def DT(filename):
   num_inst = 0                      #count number of instances
   num_attr = 0                      #count the number of attributes
   data_bool = False                 #Flag to indicate data follows
   output_cat = ""                   #record output catagory
   output_index = -1                 #record output catagory index
   types = ""
   attr_dict = {}
   attr_list = []
   data_list = []
   with open(filename, 'r') as f:
      for line in f:
         
         #count number of instances
         if data_bool == True:
            num_inst = num_inst + 1
            test = line.strip()
            test = test.split(',')
            data_list.append(test)
         if line[0:5] == "@data":
            data_bool = True
      
         #count number of attributes
         if line[0:10] == "@attribute":
            num_attr = num_attr + 1
            output_index = num_attr - 1
            type_list = [] 
            test = line.strip()
            test = test.split()
            output_cat = test[1] #will write over var each iteration
            attr_list.append(output_cat)
            attr_len = len(test[2:])
            for i in range(0, attr_len):
               types = str(test[2:][i])
               types = types.strip('{ , }')
               type_list.append(types)
            attr_dict[output_cat] = type_list

     #print(attr_dict)
      print(attr_list)
      print(data_list)
     #print("Number of instances: ", num_inst)
     # print("Number of attributes: ", num_attr)
     # print("Output Catagory and index: ", output_cat, output_index)
     

#input_file = input("Please enter file name: ")

DT("set1.data")







