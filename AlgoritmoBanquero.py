import numpy as np

m_necesidad = np.array([[5,2,2,2], [2,2,3,0], [1,2,1,1],[4,2,2,2], [3,1,1,2],[3,4,0,4]])
m_asigancion = np.array([[3,1,1,1], [1,1,2,0], [1,0,1,0], [0,2,2,1],[2,1,0,1],[1,2,0,1]])
v_recursos = np.array([9,9,6,6])

suma_asignacion = np.zeros(len(v_recursos), dtype='int') #crear un vector totalmente vacio



for c in range(len(v_recursos)): suma_asignacion[c] = np.sum(np.ndarray.flatten(m_asigancion[:, c:c+1]))  #Encontramos la suma de las respectivas columnas de 
                                                                                                            #asignacion con la cual vamos a encontrar el primer
                                                                                                            #valor del vector de disponibilidad

disponible =  v_recursos - suma_asignacion   #Primer valor del vector de disponibilidad


m_resultado = m_necesidad - m_asigancion   #Obtener el resultado de la matriz de necesidades menos(-) la de asignacion


def proceso(disponible):
	for i in range(m_resultado.shape[0]): #indica en pocas palabras el numero de procesos
		if (np.all(np.less_equal(m_resultado[i], disponible))) and (not np.any(m_resultado[i]) != True):     #np.all --> verifica que todos los valores sean distintos de cero(0) #not np.any verifica que aun existan posibles procesos a ejecutar (que no esten en cero)
			disponible += m_asigancion[i]                                                                    #np.less_equal --> devuelve el valor verdadero de la comparación x1 ≤ x2, comparando elemento a elemento
			m_necesidad[i] = np.zeros(len(v_recursos), dtype='int')    #convertir cada una de las filas indicadas en ceros(0)  
			m_asigancion[i] = np.zeros(len(v_recursos), dtype='int')
			m_resultado[i] = np.zeros(len(v_recursos), dtype='int')
			return disponible, i
			break

orden = np.zeros(m_necesidad.shape[0], dtype='int') # Crear una lista donde se almacenara el orden de 



inc = 0 
while not np.any(m_asigancion) != True:   #realizar el ciclo hasta que la matriz tenga procesos pendientes
		actualzacion_recurso, n_de_proceso_actual = proceso(disponible)
		print ("Vector de Disponibilidad: -->", actualzacion_recurso)
		orden[inc] = n_de_proceso_actual
		inc += 1
	
print("Orden de ejecucion de los procesos: ", orden)
