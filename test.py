from crease import Crease
from patternLoader import PatternLoader
from gcode import Gcode
from pattern import Pattern

# c1 = Crease((95, 20),(5, 65))
# c2 = Crease((5, 45),(95, 80))
# c3 = Crease((45, 5),(45, 95))

# creases = (c1, c2, c3)

# x = Pattern("anarchy", (100, 100), creases)

# g_list = Gcode("anarchy", x).to_string_list()
# for c in g_list:
#     print(c)

pl = PatternLoader("images/")
p = pl.loadPattern("frog.png")

#p.save_to_text("patterndb/", "frog")

g = Gcode("frog", p).to_string_list()

# for c in g:
#     print(c)

# print(sum((1,2)))


