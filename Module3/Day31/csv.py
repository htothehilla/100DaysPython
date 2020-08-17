import csv
import os

os.chdir("/Users/hillarykjuma/PycharmProjects/100DaysPython/Module3/Day31")
os.getcwd()

#data

actor = ["Alan Alda", "Loretta Swit", "Jaime Farr", "William Christopher", "Larry Linville", "Mike Farrell",
         "Gary Burghoff"]
character = ["Captain Benjamin Franklin 'Hawkeye' Pierce", "Major Margaret 'Hot Lips' Houlihan",
             "Corporal Maxwell Q Klinger", "Father Francis Mulcahy", "Major Frank Burns", "Captain B.J. Hunnicutt",
             "Corporal Walter 'Radar' O'Reilly"]
episodes = [251, 251, 216, 213, 121, 179, 177]

mash = open("mash.csv", "wt")

try:
    writer = csv.writer(mash)
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
finally:
    mash.close()

# it's important to log things to see how long they take so you know when it's finished

#spacing
mash = open("mash.csv", "wt")
try:
    writer = csv.writer(mash, lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
finally:
    mash.close()

#adding data
mash = open("mash.csv", "at")
try:
    writer = csv.writer(mash, lineterminator="\n")
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

# add a deliminiter
mash = open("mash_pipe.csv", "wt")
try:
    writer = csv.writer(mash, delimiter="|", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

mash = open("mash.tsv", "wt")
try:
    writer = csv.writer(mash, delimiter="\t", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()


