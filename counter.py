def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")
    fhand = open(file_name)
    commitDay= dict()

    for line in fhand:
        if not line.startswith("From "): continue
        line = line.split()
        # print(line)
        day = line[2]
        if day not in commitDay:
            commitDay[day] = 1
        else:
            commitDay[day] += 1
    
    print(commitDay)

## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
