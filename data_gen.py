#exercise 1
import random

def exercise1():
    container = []
    strings = ["fair","above average","below average","None","subpar","excellent","terrible"]
    for i in xrange(5000):
        thing = []
        thing.append(random.randint(-200,825))
        thing.append(random.randint(-450,9025))
        thing.append(strings[random.randint(0,len(strings)-1)])
        if not i in [3,4,5,22,47,101,177]:
            if i % 2 == 0:
                thing.append(False)
            else:
                thing.append(True)
        container.append(thing)

    with open("exercise1.csv","w") as f:
        for i in container:
            for j in i:
                f.write(str(j)+",")
            f.write("\n")

def exercise2():
    container = []
    strings = ["fair","above average","below average","None","subpar","excellent","terrible"]
    for i in xrange(5000):
        thing = []
        thing.append(random.randint(-200,825))
        thing.append(random.randint(-450,9025))
        thing.append(strings[random.randint(0,len(strings)-1)])
        if i % 2 == 0:
            if (i +2)%3 == 1:
                thing.append(False)
            else:
                thing.append(True)
        container.append(thing)

    with open("exercise2.csv","w") as f:
        for i in container:
            for j in i:
                f.write(str(j)+",")
            f.write("\n")

def exercise3():
    container = []
    strings = ["fair,","above average","below average","None,","subpar","excellent","terrible,"]
    for i in xrange(5000):
        thing = []
        thing.append(random.randint(-200,825))
        thing.append(random.randint(-450,9025))
        thing.append(strings[random.randint(0,len(strings)-1)])
        if not i in [3,4,5,22,47,101,177]:
            if i % 2 == 0:
                thing.append(False)
            else:
                thing.append(True)
        container.append(thing)

    with open("exercise3.csv","w") as f:
        for i in container:
            for ind,j in enumerate(i):
                if ind%3==0 and ind%5==0:
                    f.write(str(j)+",,")
                else:
                    f.write(str(j)+",")
            f.write("\n")

def exercise4():
    container = []
    strings = ["fair","above average","below average","None,","subpar","excellent","terrible"]
    for i in xrange(5000):
        thing = []
        thing.append(random.randint(-200,825))
        thing.append(random.randint(-450,9025))
        thing.append(strings[random.randint(0,len(strings)-1)])
        if i % 2 == 0:
            thing.append(False)
        else:
            thing.append(True)
        container.append(thing)

    with open("exercise4.csv","w") as f:
        for i in container:
            for ind,j in enumerate(i):
                f.write(str(j)+",")
            

def exercise5():
    container = []
    strings = ["fair","above average","below average","None","subpar","excellent","terrible"]
    for i in xrange(5000):
        thing = []
        thing.append(random.randint(-200,825))
        thing.append(random.randint(-450,9025))
        thing.append(strings[random.randint(0,len(strings)-1)])
        
        if i % 2 == 0:
            thing.append(False)
        else:
            thing.append(True)
        container.append(thing)

    with open("exercise5.csv","w") as f:
        for i in container:
            for ind,j in enumerate(i):
                if ind%3==0 and ind%5==0:
                    f.write(str(j)+",")
                    f.write("\n")
                else:
                    f.write(str(j)+",")

#https://www.englishclub.com/vocabulary/time-date.htm
def exercise6():
    container = []
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    months_abbrev = ["Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
    months_abbrev_dec = ["Jan.","Feb.","Mar.","Apr.","May","June","July","Aug.","Sept.","Oct.","Nov.","Dec."]
    year = []
    for i in range(1900,2100):
        year.append(str(i))
    day = []
    for i in range(1,32):
        day.append(str(i))
    
    day_th = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]
    
    for i in xrange(1000):
        date = []
        if i%3 == 0:
            date.append(day_th[random.randint(0,len(day_th))])
            date.append(months_abbrev[random.randint(0,len(months_abbrev))])
            date.append(year[random.randint(0,len(year))])
        if i%5 == 0:
            date.append(day[random.randint(0,len(day))])
            date.append(months_abbrev[random.randint(0,len(months_abbrev))])
            date.append(year[random.randint(0,len(year))])
        if i%2 == 0:
            date.append(day_th[random.randint(0,len(day_th))])
            date.append(months_abbrev_dec[random.randint(0,len(months_abbrev_dec))])
            date.append(year[random.randint(0,len(year))])
        final_date = " ".join(date)
        container.append(final_date)
    with open("exercise6.csv","w") as f:
        for i in container:
            f.write(i+"\n")
            

def exercise7():
    container = []
    for i in xrange(30):
        for i in xrange(9):
            thing = []
            num = str(random.randint(0,10))
            thing.append(num)
        if i%3 == 0:
            number = ".".join(thing)
        elif i%2 == 0:
            number = "-".join(thing)
        container.append(number)
    with open("exercise7.csv","w") as f:
        for i in container:
            f.write(str(i)+"\n")

def exercise8():
    
    names = ['Laveta', 'Lawerence', 'Deeanna', 'Starr', 'Tyron', 'Dionne', 'Sheryl', 'Tamela', 'Kelle', 'Delena', 'Chelsea', 'Angel', 'Shara', 'Waneta', 'Blaine', 'Jeannie', 'Shirley', 'Isidro', 'Kathie', 'Damon', 'Brigette', 'Hana', 'Lanita', 'Mozell', 'Becki', 'Shakita', 'Cierra', 'Marian', 'Lorilee', 'Cathrine', 'Tressie', 'Cecilia', 'Claretha', 'Shea', 'Yajaira', 'Carline', 'Orlando', 'Elidia', 'Lisha', 'Rafael', 'Trey', 'Sherie', 'Marita', 'Jenell', 'Maye', 'Tessa', 'Karen', 'Adriana', 'Yesenia', 'Rebecka']
    rules = [{"l":"k"},{"e":"r"},{"j":"q"},{"m":"r"},{"r":"t"},{"d":"t"},{"y":"e"},{"c":"h"},{"n":"d"},{"t":"r"},{"i":"er"},{"a":"e"}]
    new_names = []
    for name in names:
        new_name = []
        for indx,letter in enumerate(name):
            rule = rules[random.randint(0,len(rules)-1)]
            if letter in rule.keys():
                new_name.append(rule[letter])
            else:
                if indx%3==0:
                    num = ord(letter)
                    if num < 119:
                        num += 3
                    else:
                        num -= 3
                    new_letter = chr(num)
                    new_name.append(new_letter)
                else:
                    new_name.append(letter)
        transformed = "".join(new_name)
        new_names.append(transformed)
    with open("exercise8.csv","w") as f:
        for name in new_names:
            f.write(str(name)+"\n")

def exercise9():
    
    names = ['Laveta', 'Lawerence', 'Deeanna', 'Starr', 'Tyron', 'Dionne', 'Sheryl', 'Tamela', 'Kelle', 'Delena', 'Chelsea', 'Angel', 'Shara', 'Waneta', 'Blaine', 'Jeannie', 'Shirley', 'Isidro', 'Kathie', 'Damon', 'Brigette', 'Hana', 'Lanita', 'Mozell', 'Becki', 'Shakita', 'Cierra', 'Marian', 'Lorilee', 'Cathrine', 'Tressie', 'Cecilia', 'Claretha', 'Shea', 'Yajaira', 'Carline', 'Orlando', 'Elidia', 'Lisha', 'Rafael', 'Trey', 'Sherie', 'Marita', 'Jenell', 'Maye', 'Tessa', 'Karen', 'Adriana', 'Yesenia', 'Rebecka']
    rules = [{"l":"k"},{"e":"r"},{"j":"q"},{"m":"r"},{"r":"t"},{"d":"t"},{"y":"e"},{"c":"h"},{"n":"d"},{"t":"r"},{"i":"er"},{"a":"e"},{"b":"o"},{"e":"a"},{"s":"v"}]
    new_names = []
    for name in names:
        new_name = []
        for indx,letter in enumerate(name):
            rule = rules[random.randint(0,len(rules)-1)]
            if letter in rule.keys():
                new_name.append(rule[letter])
            else:
                if indx%3==0:
                    num = ord(letter)
                    if num < 119:
                        num += 3
                    else:
                        num -= 3
                    new_letter = chr(num)
                    new_name.append(new_letter)
                else:
                    new_name.append(letter)
        transformed = "".join(new_name)
        new_names.append(transformed)
    with open("exercise9.csv","w") as f:
        for name in new_names:
            f.write(str(name)+"\n")


if __name__=='__main__':
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
