# def parent(arg_1, arg_2):
#     # From child()'s point of view,
#     # 'value' and 'my_dict' are nonlocal variables,
#     # as are 'arg_1' and 'arg_2'
#     value = 22
#     my_dict = {'chocolate':'yummy'}
  
#     def child():
#       print(2 * value)
#       print(my_dict['chocolate'])
#       print(arg_1 + arg_2)
#     return child
      
#   my_func = parent(3, 4)
  
#   # Show that my_func()'s closure is not None
#   print([cell.cell_contents for cell in my_func.__closure__])
  
  
def return_a_func(arg1, arg2):
    def new_func():
        print('arg1 was {}'.format(arg1))
        print('arg2 was {}'.format(arg2))
    return new_func
    
my_func = return_a_func(2, 17)

# Show that my_func()'s closure is not None
print(my_func.__closure__[0].cell_contents is not None)