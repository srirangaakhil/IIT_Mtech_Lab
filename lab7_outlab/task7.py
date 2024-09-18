import matplotlib.pyplot as plt
import numpy as np

x = np.load('./message.npy')

b = 255
a = 0
c = np.amin(x)
d = np.amax(x)

y = (x - c)*(b - a)/(d - c) + a

plt.imshow(y)
#plt.show()
plt.savefig('processedimage.png')


