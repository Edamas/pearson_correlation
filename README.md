# pearson_correlation
Function in pure python

----------------------------------------------
# Example 1:

correl = correlacao(
  serie_x=[0, 1, 2, 3, 4, 5], 
  serie_y=[10, 11, 12, 13, 14, 15],
verbose=True)

# Result:
'''
n:                             6.               
soma_x:                       15.               
soma_y:                       75.               
soma_xy:                      17.5              
soma_x_quadrado:              55.               
soma_y_quadrado:             955.               
soma_xx:                      17.5              
soma_yy:                      17.5              
soma_xy:                      17.5              
CORRELAÇÃO r:                  1.0  
'''

----------------------------------------------
# Example 2:

correl = correlacao(
  serie_x=[0, 1, 2, 3, 4, 5], 
  serie_y=[10, 11, 12, 13, 14, 15],
verbose=False)
print(correl)

# Result:
1.0
