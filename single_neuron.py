#memanggil library numpy
import numpy as np

#inisialisasi input 10 layer
inputs = [6.8,9,3,5,5.8,2.5,8.8,9.2,1.9,7.2]

#inisialisasi weights sesuai jumlah neuron yaitu satu, dan panjang sesuai input layer yaitu 10
weights = [4.5,2.7,7.8,1,1.5,2.9,1.7,8.9,5,0.7]

#inisialisasi bias sesuai panjang neuron yaitu satu
bias = 3

#kalikan Weight dan input menggunakan dot lalu ditambah bias
outputs = np.dot(weights, inputs)+bias

#menampilkan hasil output
print(outputs)