import numpy as np

#-----------------------------------------------------------------------
#                        node_0
# [2] ---------(1)------> |[]|xx
#     xx      (1)zz-----> |  |  xx
#       xx  zz            |  |    (2)--->
#         xz              |  |            []
#       zz  xx            |  |    (-1)-->
#     zz      (-1)xx----> |  |  ZZ
# [3] --------(1)-------> |[]|zz
#                        node_1
#-----------------------------------------------------------------------

def relu(input):
    '''Define your 'relu' activation function here'''
    # Calculate the value for the output of the relu-function: output
    # max()-function is called with an iterable, returns the largest item of argument 'input'.
    output = max(0, input)

    # Return the value just calculated
    return(output)

#-----------------------------------------------------------------------
first_input_data = np.array([2, 3])
weights =  {
        # first hidden layer
        'node_0':np.array([1, 1]),
        'node_1':np.array([-1, 1]),
        # second hidden layer
        # 'node_3':np.array([0, 1]),
        # 'node_4':np.array([1, 1]),
        # output layer
        'output':np.array([2, -1])}

print('first_input_data: ', first_input_data)
print("weights: ", weights)
#-----------------------------------------------------------------------
# Calculate node 0 value: node_0_value
print('weights[\'node_0\']: ', weights['node_0'])
node_0_value = (first_input_data * weights['node_0']).sum()
node_0_output = relu(node_0_value)
print('node_0_output: ', node_0_output)

# Calculate node 1 value: node_1_value
print('weights[\'node_1\']', weights['node_1'])
node_1_value = (first_input_data * weights['node_1']).sum()
node_1_output = relu(node_1_value)
print('node_1_output: ', node_1_output)

# Put node values into array: hidden_layer_outputs
first_hidden_layer_outputs = np.array([node_0_output, node_1_output])
print('hidden_layer_outputs (np.array): ', first_hidden_layer_outputs)

#------------------------------------------------

# second_input_data = first_hidden_layer_outputs

# # Calculate node 0 value: node_0_value
# print('weights[\'node_3\']: ', weights['node_3'])
# node_3_value = (second_input_data * weights['node_3']).sum()
# print('node_3_value: ', node_3_value)

# # Calculate node 1 value: node_1_value
# print('weights[\'node_4\']', weights['node_4'])
# node_4_value = (second_input_data * weights['node_4']).sum()
# print('node_4_value: ', node_4_value)

# # Put node values into array: hidden_layer_outputs
# second_hidden_layer_outputs = np.array([node_3_value, node_4_value])
# print('second_hidden_layer_outputs (np.array): ', second_hidden_layer_outputs)

#------------------------------------------------

# Calculate output: output
print('weights[\'output\']: ', weights['output'])
output = (first_hidden_layer_outputs * weights['output']).sum()
print(output)
