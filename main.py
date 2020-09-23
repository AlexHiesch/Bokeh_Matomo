"""
    This example integrates a static asset,
    in this case a Matomo javascript snippet,
    in a Bokeh Webapp without the Directory-Style
    in case you have no influence over the
    startup command of Bokeh.
    This solution works therefore also with
    directly calling 'bokeh serve main.py'
"""
from jinja2 import Environment, FileSystemLoader, Template
from bokeh.io import curdoc

FILE_LOADER = FileSystemLoader('templates')
ENV = Environment(loader=FILE_LOADER)

TEMPLATE = ENV.get_template('index.html')

curdoc().template = TEMPLATE

# Alternative inline
"""
HTML = Template('''
{% extends base %}

{% block title %}Bokeh Crossfilter Example{% endblock %}

{% block preamble %}
      <!-- Matomo -->
<script type="text/javascript">
    var _paq = window._paq || [];
    /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
      var u="//someurl/matomo/";
      _paq.push(['setTrackerUrl', u+'piwik.php']);
      _paq.push(['setSiteId', '326']);
      var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
      g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js';
      s.parentNode.insertBefore(g,s);
    })();
  </script>
  <!-- End Matomo Code -->
{{text}}
{% endblock %}
''')

curdoc().template = HTML
"""