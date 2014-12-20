from IPython.core.display import display, HTML

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

def show_network(name, nodes, edges):
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
