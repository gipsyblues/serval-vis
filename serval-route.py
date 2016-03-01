import commands
import networkx as nx
import matplotlib.pyplot as plt

# DIRTY QUICK HACK: Visualize serval route print using matplotlib

G=nx.Graph()

#status, output = commands.getstatusoutput('serval-dna/servald route print')
status, output = commands.getstatusoutput('cat data/route-dump.txt')

if status != 0:
    print "error executing servald route print"
    sys.exit(1)

routingtable = []
my_sid = ""
my_sid_short = ""

# parse and add all nodes
for i in output.split("\n"):
    fields = i.split(":")
    if len(fields) == 4 and not fields[0].startswith("Sub"):
        routingtable.append(fields)
        short_name = fields[0][0:4] + "..." + fields[0][-4:]

        G.add_node(fields[0], color='blue', fillcolor='blue', short_name=short_name)

        if fields[1] == 'SELF':
            my_sid = fields[0]


print routingtable
# add all paths
for i in routingtable:
    if i[1] == 'INDIRECT':
        G.add_edge(i[0], i[3])
    elif i[1] == 'UNICAST':
        G.add_edge(i[0], my_sid)
    else:
        print "Ignoring: ", i


print "Number of nodes: ", G.number_of_nodes()
print "Number of edges: ", G.number_of_edges()

print G.nodes()
node_colors = ["blue" if n == my_sid else "red" for n in G.nodes()]
node_labels_short = {}
for i in G.nodes():
    node_labels_short[i] = i[0:4] + ".." + i[-4:]

print node_labels_short
pos = nx.spring_layout(G)

nx.draw(G, pos, node_color=node_colors, with_labels=False)

for p in pos:  # raise text positions
    pos[p][1] += 0.1

nx.draw_networkx_labels(G, pos, node_labels_short)

plt.show()
