import numpy as np

#-----------------------------------------------------------------------
#                        node_0
# [3] ---------(2)------> |[]|xx
#     xx      (0)zz-----> |  |  xx
#       xx  zz            |  |    (2)--->
#         xz              |  |            []
#       zz  xx            |  |    (2)-->
#     zz      (1)xx----> |  |  ZZ
# [2] --------(0)-------> |[]|zz
#                        node_1
#-----------------------------------------------------------------------

def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    # max(): called with an iterable, returns the largest item in it.
    output = max(0, input)

    # Return the value just calculated
    return(output)

#-----------------------------------------------------------------------
first_input_data = np.array([3, 2])
weights =  {
        # hidden layer
        'node_0':np.array([2, 1]),
        'node_1':np.array([0, 0]),

        'output':np.array([2, 2])}

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

# Calculate output: output
actual_target_value = 5
print('weights[\'output\']: ', weights['output'])
output = (first_hidden_layer_outputs * weights['output']).sum()
print("Predicted: ", output)
print("ERROR (= Predicted - ActualTargetValue): ", output - actual_target_value)
