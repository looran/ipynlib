from IPython.core.display import display, HTML

def show(name, countries):
    print("%d keys" % (len(countries)))
    display(HTML("""
<div id="%s" style="width: 1000px; height: 550px;"></div>
<!-- XXX didnt find https -->
<link rel="stylesheet" href="http://jvectormap.com/css/jquery-jvectormap-2.0.0.css" type="text/css" media="screen"/>
<script>
require.config({paths: {jvectormap: "http://jvectormap.com/js/jquery-jvectormap-2.0.0.min", // XXX didnt find https
                        worldmap: "http://jvectormap.com/js/jquery-jvectormap-world-mill-en", // XXX didnt find https
                        jquery: "https://code.jquery.com/jquery-1.11.1.min"}});
require(["jvectormap", "worldmap", "jquery"], function(jvectormap, worldmap, jquery) {
    $(function(){
        countriesdata = %s;
        $('#%s').vectorMap({
          map: 'world_mill_en',
          series: {
            regions: [{
              values: countriesdata,
              scale: ['#C8EEFF', '#0071A4'],
              normalizeFunction: 'linear',
            }]
          },
          onRegionTipShow: function(e, el, code){
            el.html(el.html()+' (%s: '+countriesdata[code]+')');
          }
        });
    }); });
</script>""" % (name, countries, name, name) ))

