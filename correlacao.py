def correlacao(serie_x, serie_y, verbose=False):
    
    assert len(serie_x) == len(serie_y)

    n = len(serie_x)
    
    soma_x = sum(serie_x)
    soma_y = sum(serie_y)
    soma_xy = sum([x * y for x, y in zip(serie_x, serie_y)])
   
    soma_x_quadrado = sum([x * x for x in serie_x])
    soma_y_quadrado = sum([y * y for y in serie_y])

    soma_xx = soma_x_quadrado - (soma_x ** 2) / n
    soma_yy = soma_y_quadrado - (soma_y ** 2) / n
    
    assert soma_xx >= 0
    assert soma_yy >= 0
    
    soma_xy = soma_xy - (soma_x * soma_y) / n
        
    r = soma_xy / (soma_xx * soma_yy) ** 0.5
    
    if verbose:
        print('n:              ', s(n))
        print('soma_x:         ', s(soma_x))
        print('soma_y:         ', s(soma_y))
        print('soma_xy:        ', s(soma_xy))
        print('soma_x_quadrado:', s(soma_x_quadrado))
        print('soma_y_quadrado:', s(soma_y_quadrado))
        print('soma_xx:        ', s(soma_xx))
        print('soma_yy:        ', s(soma_yy))
        print('soma_xy:        ', s(soma_xy))
        print('CORRELAÇÃO r:   ', s(r))
    return r

# Example:
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

