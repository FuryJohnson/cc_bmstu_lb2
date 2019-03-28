from grammar import fromJSON

"Импортирую грамматику через JSON"


g = fromJSON('grammars/2.4.19.json')

print(g)
print(g.isInGNF())

# g.eliminateIdentity()

# g.eliminateLeftRecursion()

newg = g.toGNF()

print(newg)

print(newg.isInGNF())
