# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

# Own try =  print(basket[0][2])


#erklärung GPT4.5


#Deine Überlegung ist fast richtig, aber der Zugriff auf das Element "Oranges" in der verschachtelten Liste funktioniert etwas anders, weil "Oranges" sich nicht in der ersten Liste (basket[0]), sondern in einer tiefer verschachtelten Liste befindet.

# Schauen wir uns die Struktur von basket genauer an:

#python
#Copy code
#basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
#basket[0] gibt dir "Banana", weil das erste Element in basket die Zeichenkette "Banana" ist.
#basket[1] gibt dir die Liste ["Apples", ["Oranges"], "Blueberries"], weil das zweite Element in basket eine weitere Liste ist.
#Jetzt betrachten wir die Liste, die in basket[1] enthalten ist:

#python
#Copy code
#["Apples", ["Oranges"], "Blueberries"]
#basket[1][0] ist "Apples".
#basket[1][1] ist ["Oranges"] (eine Liste, die nur das Element "Oranges" enthält).
#basket[1][2] ist "Blueberries".
#Um also "Oranges" zu erreichen, musst du wie folgt vorgehen:

#basket[1] gibt dir die Liste ["Apples", ["Oranges"], "Blueberries"].
#basket[1][1] gibt dir die Liste ["Oranges"].
#basket[1][1][0] gibt dir schließlich "Oranges".
#Daher lautet der richtige Befehl:

#python
#Copy code
#print(basket[1][1][0])
#Dieser Code gibt "Oranges" aus.


































# Solution:
# basket[1][1][0]
