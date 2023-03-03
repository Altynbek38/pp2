import re
def f(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()
text = "mySuperVarTwo" #camel case
pattern = "(?P<g1>[a-z])(?P<g2>[A-Z])+"
print(re.sub(pattern, f, text))