from IPython.core.display import display, HTML
import networkx as nx
import matplotlib.pyplot as plt

commonjs = """<script type="text/javascript">
require.config({paths: {visjs: "https://cdn.rawgit.com/almende/vis/master/dist/vis.min",
                        jquery: "https://code.jquery.com/jquery-1.11.1.min"}});
define("draw_graph", ["visjs", "jquery"], function(visjs, jquery) {
    var options = {
        width: '1000px',
        height: '900px',
        nodes: {
          shape: 'dot',
          fontFace: "Tahoma"
        },
        edges: {
           inheritColor: "from"
        },
        clustering: {
            enabled: false,
        },
        tooltip: {
            delay: 300,
        },
        stabilize: false,
        //hideEdgesOnDrag: true
    };
    return function draw_graph(gephiJSON, divid) {
        var data = visjs.network.gephiParser.parseGephi(gephiJSON, {allowedToMove: true, parseColor: false});
        var container = document.getElementById(divid);
        var network = new visjs.Network(container, data, options);
    };
});
</script>"""

def show_js(name, nodes, edges):
    print("%d nodes\n%d edges" % (len(nodes), len(edges)))
    display(HTML(commonjs + 
"""<button type="button" id="%s_button">Show/Hide</button>
<div id="%s"></div>
<script type="text/javascript">
$( "#%s_button" ).click(function() {
    $( "#%s" ).toggle();
});
require(["draw_graph"], function(dg) { dg(%s, '%s'); });
</script>""" % (name, name, name, name, json.dumps({ "nodes": nodes, "edges": edges }), name) ))

def show_py(nodes, edges, width, height, outfile):
    g = nx.Graph()
    labels = dict()
    colors = list()
    sizes = list()
    for e in nodes:
        g.add_node(e["id"])
        g.node[e["id"]]['color'] = e["color"]
        g.node[e["id"]]['size'] = e["size"]
        labels[e["id"]] = e["label"]
    for e in edges:
        g.add_edge(e["source"], e["target"])

    for n in g.nodes():
        colors.append(g.node[n]["color"])
        sizes.append(g.node[n]["size"])

    print "XXX 0"
    plt.figure(figsize=(width,height));
    print "XXX 1"
    pos = nx.graphviz_layout(g)
    print "XXX 2"
    gx = nx.draw_networkx(g, pos, labels=labels, node_size=sizes, node_color=colors, font_size=7, font_color="black", edge_color="grey")
    #gx = nx.draw_networkx(g, labels=labels, node_size=sizes, node_color=colors, font_size=7, font_color="black", edge_color="grey")
    print "XXX 3"
    s = plt.savefig(outfile, bbox_inches="tight")
    #s = plt.savefig(outfile)
    print "XXX 4"
