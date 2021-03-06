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
   pretty_inst = 'Number of instances: {}'.format(num_inst)
   print(pretty_inst)
   
   #FIND ATTRIBUTE NODE
   root_node = ""
   gain = 0
   bool_dict = {}
   for attr in range(0, num_attr - 1):
      total_overall = 0
      remainder = 0
      calculations_dict = {}
      curr_attr = attr_list[attr]
      attr_types = attr_dict[curr_attr]
     #print(curr_attr)
      for type in attr_types:
         bool_list = []
         true_count = 0.0
         false_count = 0.0
         for i in range(0, num_inst): #iterate through data
            if type in data_list[i]:
               if data_list[i][output_index] == "T":
                  true_count = true_count + 1
                  total_overall = total_overall + 1
               else:
                  false_count = false_count + 1
                  total_overall = total_overall + 1
         bool_list.append(true_count)
         bool_list.append(false_count)
         bool_dict[type] = bool_list
        #print("type: ", type, "true: ", true_count, "false: ", false_count)
         if (true_count > 0 and false_count > 0):
            calc_list = []
            true_num = true_count
            false_num = false_count
            log_denom = (true_count + false_count)
            true_log = (-true_num/log_denom) * math.log(true_num/log_denom,2)
            false_log = (-false_num/log_denom) * math.log(false_num/log_denom,2)
            log_calc = (true_log + false_log)
            calc_list.append(log_calc)
            calc_list.append(log_denom)
            calculations_dict[type] = calc_list
 
      #finish calculations
      for type in attr_types:
         if type in calculations_dict:
            val_list = calculations_dict[type]
            log_val = val_list[0]
            total_val = val_list[1]
            outer_frac = (total_val/total_overall)
            remainder += (outer_frac * log_val)
      new_gain = 1 - remainder
      if (new_gain > gain):
         gain = new_gain
         root_node = curr_attr
      pretty_gain = 'Attribute: {} Gain: {}'.format(curr_attr, new_gain)
      print(pretty_gain)
   pretty_root = '{} {}'.format('Root Node: ', root_node)
   print(pretty_root)
   node_types = attr_dict[root_node]
   for type in node_types:
     true_v = bool_dict[type][0]
     false_v = bool_dict[type][1]
     if (true_v == 0):
        pretty_leaf = 'Leaf {}: F ({})'.format(type, false_v)
        print(pretty_leaf)
     elif (false_v == 0):
        pretty_leaf = 'Leaf {}: T ({})'.format(type, true_v)
        print(pretty_leaf)   
      
  #print(bool_dict)
   attr_list.remove(root_node)
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

DT("set3.data")
#DT(input_file)

