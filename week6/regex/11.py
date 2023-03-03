import re
import csv

result = [["Order", "Name", "Total"]]

file = open('row.txt', 'r', encoding="utf8")

text = file.read()
file.close()

bin_pattern = r"\nБИН\s+([0-9]{12})"
kassa_pattern = r"\nКасса\s+([0-9]{3}[-][0-9]{3})"

bin_value = re.search(bin_pattern, text)
kassa_value = re.search(kassa_pattern, text)

print(bin_value.group(0))
print(kassa_value.group(0))

BINPattern = r"\nБИН\s+(?P<BIN>[0-9]{12})"
KassaPattern = r"\nКасса\s+(?P<Kassa>.+)"

BINValue = re.search(BINPattern, text).group("BIN")
KassaValue = re.search(KassaPattern, text).group("Kassa")

print(BINValue)
print(KassaValue)