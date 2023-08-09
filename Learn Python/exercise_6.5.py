text = "X-DSPAM-Confidence:    0.8475"
y = text.find("0")
text2 = text[23:]
b = float(text2)
print(b)