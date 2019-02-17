from objects.crease import Crease
from objects.pattern import Pattern
from objects.gcode import Gcode

c1 = Crease((95, 20),(5, 65))
c2 = Crease((5, 45),(95, 80))
c3 = Crease((45, 5),(45, 95))

creases = (c1, c2, c3)

x = Pattern("anarchy", (100, 100), creases)

g_list = Gcode("anarchy", x).to_string_list()
for c in g_list:
    print(c)