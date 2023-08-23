## 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.


fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0

for each_line in fh:
    each_line = each_line.rstrip()
    if each_line.startswith("X-DSPAM-Confidence:"):
        colon_index = each_line.find(":")
        confidence_value = float(each_line[colon_index+1:].strip())
        total += confidence_value
        count += 1

if count != 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No X-DSPAM-Confidence lines found in the file.")

fh.close()