#Test the math table

import fontforge

font=fontforge.font()
math = font.math

if math.exists():
  raise ValueError("Thinks there is a math table in an empty font")
math.clear()

math.ScriptPercentScaleDown = 3
math.SubscriptBaselineDropMin = 6
if not math.exists():
  raise ValueError("Thinks there isn't a math table after we added one")
if ( math.ScriptPercentScaleDown!=3 or math.SubscriptBaselineDropMin != 6) :
  raise ValueError("Assignment failed")

math.clear()
if math.exists():
  raise ValueError("Thinks there is a math table in an empty font")

a = font.createChar(65)
c = font.createChar(67)
a.horizontalVariants = "B C D"
a.horizontalComponents = (("a",),("b",1,20,20,200),c)
a.horizontalComponentItalicCorrection = 10

a.verticalVariants = "B.v C.v D.v"
a.verticalComponents = (("a",),("b",1,20,20,200),c)
a.verticalComponentItalicCorrection = 20

if a.horizontalVariants != "B C D" or a.horizontalComponentItalicCorrection!=10:
  raise ValueError("Failed to set some glyph horizontal variant/component")
if a.verticalVariants != "B.v C.v D.v" or a.verticalComponentItalicCorrection!=20:
  raise ValueError("Failed to set some glyph vertical variant/component")

# non-regression test for a bad allocation in ParseComponentTuple
font[65].horizontalComponents = (('a',))
font[65].verticalComponents = (('a',))

#print a.verticalComponents
#print a.mathKern.topLeft

#a.mathKern.topLeft = ((1,2),(2,3))
#print a.mathKern.topLeft
#print a.mathKern.topRight
