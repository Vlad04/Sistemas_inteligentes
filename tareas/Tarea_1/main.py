from state import State
import search
import time
import resource


def path(last_pos):
    position = last_pos.prev
    next_pos = last_pos

    path = []

    while position != None:
        if position.node.up() == next_pos.node:
            path.append("Up")
        elif position.node.down() == next_pos.node:
            path.append("Down")
        elif position.node.left() == next_pos.node:
            path.append("Left")
        elif position.node.right() == next_pos.node:
            path.append("Right")

        position = position.prev
        next_pos = next_pos.prev

    return path[::-1]


tiempo_inicio = time.time()
config = [1,2,5,3,4,0,6,7,8]

game = State(config)

result = search.bfs(game)
final_pos = result.position
max_depth = result.max_depth
nodes_expanded = result.nodes_expanded

print "Path to goal", path(final_pos)
print "Cost to the path", final_pos.cost
print "Number of expanded-visited nodes", nodes_expanded
print "Running time in secs", time.time() - tiempo_inicio
print "Memory usage", resource.getrusage(1)[2]


