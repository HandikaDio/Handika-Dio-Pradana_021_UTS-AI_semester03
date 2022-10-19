#memanggil library numpy
import numpy as np

#inisialisasi input 10 layer
inputs = [5, 4, 3, 5.4, 6, 2, 5.3, 9, 1, 8]
 
#inisialisasi weight sesuai jumlah neuron yaitu 5, dan panjang sesuai input layer yaitu 10
weights = [[-4.3, 4.1, 8, 9.2, 4.2, -6.2, 6, 2, 6.5, 5.1],
           [5.1, 2.3, 5.4, 8.7, -2.3, 7.6, 3.8, 7.9, -2.1, 4.5],
           [1.7, -3, 5.6, 8, 3.1, 2.6, 7.6, 8.9, 6.4, -4.5]
           [0.1, -2.3, 2.4, 1.5, 4.6, -5.7, 2, 6.8, 4.9, 0.6]]

#inisialisasi bias sesuai panjang neuron yaitu 5
biases = [4, 8, 7.1, -4.2, 5.3]

#kalikan Weight dan input menggunakan dot lalu ditambah bias
output = np.dot(weights, inputs)+biases

#tampilkan hasil output
print(output)