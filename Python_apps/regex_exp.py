from cgitb import text
import re
txt="""Print the NO- 1112333 part of the string where there was a match.
The regular NO- 345 expression looks no-4 for any words NO-7654 that starts with an upper case """

# reg=re.findall(r'no-[0-9]*',txt)
reg=re.findall(r'[A-Z]+[-| ]*[0-9]*',txt)
reg=re.findall(r'[A-Z]+[-| ]*\d *',txt)

# reg=re.findall(r"[P][a-z]+",txt)


print(reg)
