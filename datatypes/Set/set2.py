#Set Methods

course = {'java','python','c++','php','angular'}
#add element  in the set
# course.add('react')
# print('add method',course)

more_coures = {'cloud coumputing','Digital marckting'}
#updated method :adding items
course.update(more_coures)
print(course)

#discard method:remove the spacifide element
course.discard('c++')
print(course)

#pop method: it will remove randome value 
course.pop()
print(course)

#remove method:remove the spacifide element
print(course)
course.remove('java')
print('remove method from the coures', course)

ice_cream={'vanila','choc-chips','mango','conconut'}
more_ice_cream= {'BUtterscotch','coconut', 'rojbhog','mango'}

#Return all items of both the set

union_method = ice_cream.union(more_ice_cream)
print(union_method)

#using oprator |

union_method = ice_cream| more_ice_cream
print('Union method using oprator:', union_method)