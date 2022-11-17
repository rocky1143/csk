from collections import defaultdict
jug1=int(input("Enter capacity of j1 : "))
jug2=int(input("Enter capcity of j2 : "))
aim=int(input("Aim"))
def deaf():
	return False
visited = defaultdict(deaf)
def waterJugSolver(amt1, amt2):
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print('(',amt1, amt2,')')
		return True
	if visited[(amt1, amt2)] == False:
		print('(',amt1, amt2,')',end="-->")
		visited[(amt1, amt2)] = True
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	else:
		return False
print("Steps: ")
waterJugSolver(0, 0)

'''Output
Enter capacity of j1 : 3
Enter capcity of j2 : 4
Aim: 2
Steps: 
( 0 0 )-->( 3 0 )-->( 3 4 )-->( 0 4 )-->( 3 1 )-->( 0 1 )-->( 1 0 )-->( 1 4 )-->( 3 2 )-->( 0 2 )
True '''
