import math

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
     #print(data_list)
   print("Number of instances: ", num_inst)
     # print("Number of attributes: ", num_attr)
     # print("Output Catagory and index: ", output_cat, output_index)
   
   #FIND ATTRIBUTE NODE

   for attr in range(0, num_attr - 1):
      total_overall = 0
      remainder = 0
      calculations_dict = {}
      curr_attr = attr_list[attr]
      attr_types = attr_dict[curr_attr]
      print(curr_attr)
      print("type total: ", type_total)
      for type in attr_types:
         true_count = 0.0
         false_count = 0.0
         for i in range(0, num_inst):
            if type in data_list[i]:
               if data_list[i][output_index] == "T":
                  true_count = true_count + 1
                  total_overall = total_overall + 1
               else:
                  false_count = false_count + 1
                  total_overall = total_overall + 1
         print("type: ", type, "true: ", true_count, "false: ", false_count)
         if (true_count > 0 and false_count > 0):
            true_num = true_count
            false_num = false_count
            log_denom = (true_count + false_count)
            true_log = (-true_num/log_denom) * math.log(true_num/log_denom,2)
            false_log = (-false_num/log_denom) * math.log(false_num/log_denom,2)
            log_calc = (true_log + false_log)
            
#data_entropy += (-freq/len(data))*math.log(freq/len(data),2)
#example of using log
 
'''
num1 = 2.0
num2 = 1.0
denom = 3.0
total = 5.0
outside_frac = (denom/total)
para1 = (-num1/denom) * math.log(num1/denom,2)
para2 = (-num2/denom) * math.log(num2/denom,2)
remainder = outside_frac * (para1 + para2)
gain = 1 - remainder
print("gain: ", gain)  
'''
#input_file = input("Please enter file name: ")

DT("set1.data")
#DT(input_file)

