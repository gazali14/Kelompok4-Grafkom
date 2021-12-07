import numpy as np
import matplotlib.pyplot as plt

x1 = int(input('Masukan nilai x1  : '))
y1 = int(input('Masukan nilai y1  : '))
x2 = int(input('Masukan nilai x2  : '))
y2 = int(input('Masukan nilai y2  : '))

print('------------------------------------------------')

nilaiY = y2 - y1
nilaiX = x2 - x1
N = x2 - x1 + 1

x = x1
y = y1
i = 1

if x1 == x2:
  titikX = []
  titikY = []
  while i < y2:
    if y1 == y2:
      print('Titik yang dilewati yaitu', x,',', y )
      titikX.append(x)
      titikY.append(y)
    else:
      print('Titik yang dilewati yaitu', x,',', y+i )
      titikX.append(x)
      titikY.append(y+i)
    i+=1
  plt.plot(titikX,titikY)
  plt.scatter(titikX,titikY)
  plt.grid()
  plt.show()
  
elif y1 == y2:
    titikX = []
    titikY = []
    while i < y2:
        if x1 == x2:
            print('Titik yang di lewati yaitu (',x,',',y,')')
            titikX.append(x)
            titikY.append(y)
        else:
            print('Titik yang di lewati yaitu (',x,',',y,')')
            titikX.append(x+i)
            titikY.append(y)
        i+=1
    plt.plot(titikX,titikY)
    plt.scatter(titikX,titikY)
    plt.grid()
    plt.show()
else:
    titikX = []
    titikY = []
    while i <= N:
        m = nilaiY / nilaiX
        rumusY = m * (x - x1) + y1
        kordinatY = round(rumusY)
        x+=1
        print('Titik yang di lewati yaitu (',x-1,',',kordinatY,')')
        titikX.append(x-1)
        titikY.append(kordinatY)
        i+=1
    plt.plot(titikX,titikY)
    plt.scatter(titikX,titikY)
    plt.grid()
    plt.show()
