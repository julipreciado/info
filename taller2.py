import numpy as np
import matplotlib.pyplot as plt
#señales:
n=np.arange(101)
y=np.sin(np.pi*0.12*n)
y2=np.cos(2*np.pi*0.003*n)
s=y+y2
t=y*y2
#print(t)

#graficar señales
fig, ax=plt.subplots()
ax.plot(y,y2, color="red")
ax.set_xlabel("y")
ax.set_ylabel("y2")
ax.set_title("gráfica")

fig, ax=plt.subplots()
ax.scatter(y,y2, color="green")
#plt.show()

import cv2
import numpy as np
bgr = np.zeros((300, 300, 3), dtype=np.uint8)
bgr[:,:,:] = (255, 0, 100)
cv2.imshow('BGR', bgr)
cv2.waitKey(0)


bgr1 = np.zeros((300, 250, 3), dtype=np.uint8)
bgr1[:,:,:] = (255, 100, 100)
cv2.imshow('BGR1', bgr1)
cv2.waitKey(0)
cv2.destroyAllWindows()