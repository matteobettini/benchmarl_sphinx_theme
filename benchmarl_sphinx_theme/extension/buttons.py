from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList


class DiscordButton(Directive):
    option_spec = {
        "title": directives.unchanged,
        "url": directives.unchanged,
    }

    def run(self):
        title = self.options.get("title", "Join our Discord community!")
        url = self.options.get("url", "https://discord.com/invite/2XJdEenU")

        rst = DISCORD_TEMPLATE.format(title=title, url=url)

        callout_list = StringList(rst.split("\n"))
        callout = nodes.paragraph()
        self.state.nested_parse(callout_list, self.content_offset, callout)
        return [callout]


class ExampleButton(Directive):
    option_spec = {
        "title": directives.unchanged,
        "url": directives.unchanged,
    }
    has_content = True

    def run(self):
        url = "\n".join(self.content)
        title = self.options.get("title", "Example")
        url = self.options.get("url", url)

        rst = EXAMPLE_TEMPLATE.format(title=title, url=url)

        callout_list = StringList(rst.split("\n"))
        callout = nodes.paragraph()
        self.state.nested_parse(callout_list, self.content_offset, callout)
        return [callout]


DISCORD_TEMPLATE = """
.. raw:: html

    <a class="discord-button" href="{url}" target="_blank" title="{title}" style="display: inline-flex; align-items: center; justify-content: center;">
    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 127.14 96.36" style="vertical-align: middle; margin-right: 7px;">
        <path fill="#fff" d="M107.7,8.07A105.15,105.15,0,0,0,81.47,0a72.06,72.06,0,0,0-3.36,6.83A97.68,97.68,0,0,0,49,6.83,72.37,72.37,0,0,0,45.64,0,105.89,105.89,0,0,0,19.39,8.09C2.79,32.65-1.71,56.6.54,80.21h0A105.73,105.73,0,0,0,32.71,96.36,77.7,77.7,0,0,0,39.6,85.25a68.42,68.42,0,0,1-10.85-5.18c.91-.66,1.8-1.34,2.66-2a75.57,75.57,0,0,0,64.32,0c.87.71,1.76,1.39,2.66,2a68.68,68.68,0,0,1-10.87,5.19,77,77,0,0,0,6.89,11.1A105.25,105.25,0,0,0,126.6,80.22h0C129.24,52.84,122.09,29.11,107.7,8.07ZM42.45,65.69C36.18,65.69,31,60,31,53s5-12.74,11.43-12.74S54,46,53.89,53,48.84,65.69,42.45,65.69Zm42.24,0C78.41,65.69,73.25,60,73.25,53s5-12.74,11.44-12.74S96.23,46,96.12,53,91.08,65.69,84.69,65.69Z"/>
    </svg>
    {title}
    </a>
"""  # noqa: E501

EXAMPLE_TEMPLATE = """
.. raw:: html

  <a class="example-button" href="{url}" target="_blank" title="{title} style="display: inline-flex; align-items: center; justify-content: center;">

    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 127.14 96.36" style="margin-right: 7px;
      <defs
         id="defs4">
        <linearGradient
           id="linearGradient2795">
          <stop
             style="stop-color:#b8b8b8;stop-opacity:0.49803922;"
             offset="0"
             id="stop2797" />
          <stop
             style="stop-color:#7f7f7f;stop-opacity:0;"
             offset="1"
             id="stop2799" />
        </linearGradient>
        <linearGradient
           id="linearGradient2787">
          <stop
             style="stop-color:#7f7f7f;stop-opacity:0.5;"
             offset="0"
             id="stop2789" />
          <stop
             style="stop-color:#7f7f7f;stop-opacity:0;"
             offset="1"
             id="stop2791" />
        </linearGradient>
        <linearGradient
           id="linearGradient3676">
          <stop
             style="stop-color:#b2b2b2;stop-opacity:0.5;"
             offset="0"
             id="stop3678" />
          <stop
             style="stop-color:#b3b3b3;stop-opacity:0;"
             offset="1"
             id="stop3680" />
        </linearGradient>
        <linearGradient
           id="linearGradient3236">
          <stop
             style="stop-color:#f4f4f4;stop-opacity:1"
             offset="0"
             id="stop3244" />
          <stop
             style="stop-color:white;stop-opacity:1"
             offset="1"
             id="stop3240" />
        </linearGradient>
        <linearGradient
           id="linearGradient4671">
          <stop
             style="stop-color:#ffd43b;stop-opacity:1;"
             offset="0"
             id="stop4673" />
          <stop
             style="stop-color:#ffe873;stop-opacity:1"
             offset="1"
             id="stop4675" />
        </linearGradient>
        <linearGradient
           id="linearGradient4689">
          <stop
             style="stop-color:#5a9fd4;stop-opacity:1;"
             offset="0"
             id="stop4691" />
          <stop
             style="stop-color:#306998;stop-opacity:1;"
             offset="1"
             id="stop4693" />
        </linearGradient>
        <linearGradient
           x1="224.23996"
           y1="144.75717"
           x2="-65.308502"
           y2="144.75717"
           id="linearGradient2987"
           xlink:href="#linearGradient4671"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)" />
        <linearGradient
           x1="172.94208"
           y1="77.475983"
           x2="26.670298"
           y2="76.313133"
           id="linearGradient2990"
           xlink:href="#linearGradient4689"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4689"
           id="linearGradient2587"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)"
           x1="172.94208"
           y1="77.475983"
           x2="26.670298"
           y2="76.313133" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4671"
           id="linearGradient2589"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)"
           x1="224.23996"
           y1="144.75717"
           x2="-65.308502"
           y2="144.75717" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4689"
           id="linearGradient2248"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)"
           x1="172.94208"
           y1="77.475983"
           x2="26.670298"
           y2="76.313133" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4671"
           id="linearGradient2250"
           gradientUnits="userSpaceOnUse"
           gradientTransform="translate(100.2702,99.61116)"
           x1="224.23996"
           y1="144.75717"
           x2="-65.308502"
           y2="144.75717" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4671"
           id="linearGradient2255"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(0.562541,0,0,0.567972,-11.5974,-7.60954)"
           x1="224.23996"
           y1="144.75717"
           x2="-65.308502"
           y2="144.75717" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4689"
           id="linearGradient2258"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(0.562541,0,0,0.567972,-11.5974,-7.60954)"
           x1="172.94208"
           y1="76.176224"
           x2="26.670298"
           y2="76.313133" />
        <radialGradient
           inkscape:collect="always"
           xlink:href="#linearGradient2795"
           id="radialGradient2801"
           cx="61.518883"
           cy="132.28575"
           fx="61.518883"
           fy="132.28575"
           r="29.036913"
           gradientTransform="matrix(1,0,0,0.177966,0,108.7434)"
           gradientUnits="userSpaceOnUse" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4671"
           id="linearGradient1475"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(0.562541,0,0,0.567972,-14.99112,-11.702371)"
           x1="150.96111"
           y1="192.35176"
           x2="112.03144"
           y2="137.27299" />
        <linearGradient
           inkscape:collect="always"
           xlink:href="#linearGradient4689"
           id="linearGradient1478"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(0.562541,0,0,0.567972,-14.99112,-11.702371)"
           x1="26.648937"
           y1="20.603781"
           x2="135.66525"
           y2="114.39767" />
        <radialGradient
           inkscape:collect="always"
           xlink:href="#linearGradient2795"
           id="radialGradient1480"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(1.7490565e-8,-0.23994696,1.054668,3.7915457e-7,-83.7008,142.46201)"
           cx="61.518883"
           cy="132.28575"
           fx="61.518883"
           fy="132.28575"
           r="29.036913" />
      </defs>
      <path
         style="fill:url(#linearGradient1478);fill-opacity:1"
         d="M 54.918785,9.1927421e-4 C 50.335132,0.02221727 45.957846,0.41313697 42.106285,1.0946693 30.760069,3.0991731 28.700036,7.2947714 28.700035,15.032169 v 10.21875 h 26.8125 v 3.40625 h -26.8125 -10.0625 c -7.792459,0 -14.6157588,4.683717 -16.7499998,13.59375 -2.46181998,10.212966 -2.57101508,16.586023 0,27.25 1.9059283,7.937852 6.4575432,13.593748 14.2499998,13.59375 h 9.21875 v -12.25 c 0,-8.849902 7.657144,-16.656248 16.75,-16.65625 h 26.78125 c 7.454951,0 13.406253,-6.138164 13.40625,-13.625 v -25.53125 c 0,-7.2663386 -6.12998,-12.7247771 -13.40625,-13.9374997 C 64.281548,0.32794397 59.502438,-0.02037903 54.918785,9.1927421e-4 Z m -14.5,8.21875012579 c 2.769547,0 5.03125,2.2986456 5.03125,5.1249996 -2e-6,2.816336 -2.261703,5.09375 -5.03125,5.09375 -2.779476,-1e-6 -5.03125,-2.277415 -5.03125,-5.09375 -10e-7,-2.826353 2.251774,-5.1249996 5.03125,-5.1249996 z"
         id="path1948" />
      <path
         style="fill:url(#linearGradient1475);fill-opacity:1"
         d="m 85.637535,28.657169 v 11.90625 c 0,9.230755 -7.825895,16.999999 -16.75,17 h -26.78125 c -7.335833,0 -13.406249,6.278483 -13.40625,13.625 v 25.531247 c 0,7.266344 6.318588,11.540324 13.40625,13.625004 8.487331,2.49561 16.626237,2.94663 26.78125,0 6.750155,-1.95439 13.406253,-5.88761 13.40625,-13.625004 V 86.500919 h -26.78125 v -3.40625 h 26.78125 13.406254 c 7.792461,0 10.696251,-5.435408 13.406241,-13.59375 2.79933,-8.398886 2.68022,-16.475776 0,-27.25 -1.92578,-7.757441 -5.60387,-13.59375 -13.406241,-13.59375 z m -15.0625,64.65625 c 2.779478,3e-6 5.03125,2.277417 5.03125,5.093747 -2e-6,2.826354 -2.251775,5.125004 -5.03125,5.125004 -2.76955,0 -5.03125,-2.29865 -5.03125,-5.125004 2e-6,-2.81633 2.261697,-5.093747 5.03125,-5.093747 z"
         id="path1950" />
      <ellipse
         style="opacity:0.44382;fill:url(#radialGradient1480);fill-opacity:1;fill-rule:nonzero;stroke:none;stroke-width:15.4174;stroke-miterlimit:4;stroke-dasharray:none;stroke-opacity:1"
         id="path1894"
         cx="55.816761"
         cy="127.70079"
         rx="35.930977"
         ry="6.9673119" />
    </svg>
    {title}
  </a>
"""  # noqa: E501
