#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picturelist = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


Hier hatte ich logig Fehler: code funktioniert nicht weil 
Der Fehler liegt in der Logik deiner Schleife. In deinem Code iterierst du über die einzelnen Zeilen der picturelist, aber versuchst dann, 
diese Zeilen direkt mit 0 oder 1 zu vergleichen, was nicht funktioniert, weil jede Zeile in picturelist eine Liste ist (nicht ein einzelnes Element).

for i in picturelist:
  if (i == 0):
   print ()
  if (i == 1):
   print ("*")
  else:
    break

Fixed Code:

for row in picturelist:  # Iteriere über jede Zeile
  for i in row:  # Iteriere über jedes Element in der Zeile
    if i == 0:
      print(" ", end="")  # Gib ein Leerzeichen aus, aber bleib in der Zeile
    elif i == 1:
      print("*", end="")  # Gib ein Sternchen aus, aber bleib in der Zeile
  print()  # Gehe nach der Zeile in die nächste Zeile
