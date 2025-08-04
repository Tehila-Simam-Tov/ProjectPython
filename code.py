pluse = lambda x: x + 1
minuse = lambda x: x - 1


def costToInt(x):
    '''the function del with cases that the user enter string theat python
    doesn't can to cast to int'''
    try:
        x = int(x)
    except:
        print("שגיאה הקשת תשובה שגויה,נסה שוב:")
        x = input()
        costToInt(x)
    return x


def lateTime(nameDict, chooseing, count, leth, i, index):
    '''the function pasibel chose ansower leth time'''
    chekeInput(nameDict, chooseing, count, leth, i, index)
    if i in leth:
        leth.remove(i)
        index = index - 1


def lastTime(nameDict, chooseing, count, leth, index):
    '''in the end the function applicant to the user to ansower on
    the Qushteins theat he didn't ansower'''
    for i in range(len(leth)):
        lateTime(nameDict, chooseing, count, leth, leth[0], index)  # leth[i]


def chengeAnsowr(nameDict, chooseing, count, leth, index):
    '''the function chage the choose answer to the new choosing of the user'''
    numAnswer = input(print("הכנס את מספר התשובה שהנך רוצה לשנות:"))
    numAnswer = costToInt(numAnswer)
    while numAnswer < 1 or numAnswer > 15:
        print("תשובה שגויה,נסה שוב:")
        numAnswer = input()
        numAnswer = costToInt(numAnswer)

    temp = chooseing[numAnswer]
    # print('temp',temp)
    if temp == "":
        print('yes', temp, numAnswer)
        lateTime(nameDict, chooseing, count, leth, numAnswer, index)
    elif nameDict[numAnswer][0] == temp:
        chooseing[numAnswer] = nameDict[numAnswer][1]
        # countRishmi = countRishmi -1
        # countNoRishmi=countNoRishmi+1
        count[0] = minuse(count[0])
        count[1] = pluse(count[1])

    else:
        chooseing[numAnswer] = nameDict[numAnswer][0]
        # countRishmi = countRishmi+1
        # countNoRishmi = countNoRishmi-1
        count[0] = pluse(count[0])
        count[1] = minuse(count[1])


def cheke(nameDict, chooseing, count, leth, index):
    '''the function start to activate the exeam '''
    for i in range(1, len(nameDict) + 1):
        chekeInput(nameDict, chooseing, count, leth, i, index)


def calculation(x, y):
    '''the function cheke according to the result of x and y which type the user conect
    and what the secent type of he
    in the start the functiom find the maily type and to all type
     she serch the secend type from 4 the types'''
    mainType = ""
    secendType = ""
    ###### הכל ######
    if x == 0 and y == 0:
        print("אתה 4 סגנונות :מנתח,מקדם,משימתי ותומך")
    ###### מנתח ######
    elif x >= 0 and y <= 0:
        mainType = "מנתח"
        if x <= 7.5:
            if y >= -7.5:
                secendType = "מקדם"
            else:
                secendType = "משימתי"
        else:
            if y > -7.5:
                secendType = "תומך"
            else:
                secendType = "מנתח"
    #####תומך####
    elif x >= 0 and y >= 0:
        mainType = "תומך"
        if x <= 7.5:
            if y <= 7.5:
                secendType = "משימתי"
            else:
                secendType = "מקדם"
        else:
            if y <= 7.5:
                secendType = "מנתח"
            else:
                secendType = "תומך"
    ######משימתי#########
    elif x <= 0 and y <= 0:
        mainType = "משימתי"
        if x >= -7.5:
            if y >= -7.5:
                secendType = "תומך"
            else:
                secendType = "מנתח"
        else:
            if y >= -7.5:
                secendType = "מקדם"
            else:
                secendType = "משימתי"
    ######מקדם#######
    else:
        mainType = "מקדם"
        if x >= -7.5:
            if y >= 7.5:
                secendType = "תומך"
            else:
                secendType = "מנתח"
        else:
            if y >= 7.5:
                secendType = "מקדם"
            else:
                secendType = "משימתי"
    print('סגנון התקשורת שמאפיין אותך הוא:', mainType)
    print('והסגנון המשני:', secendType)


def chekeInput(nameDict, chooseing, count, leth, i, index):
    '''the function cheke the input of the user and decide what he went'''
    print("שאלה מספר", i, ":")
    print("אם אתה יותר", nameDict[i][0], 'הכנס: 1', "ואם אתה יותר", nameDict[i][1], 'הכנס: 2')
    choose = input()
    choose = costToInt(choose)
    while choose not in (0, 1, 2, 3):
        print("תשובה שגויה,נסה שוב:")
        choose = input()
        choose = costToInt(choose)
        # choose=int(input())
    if choose == 1:
        # countRishmi = countRishmi+1
        chooseing[i] = nameDict[i][0]
        # print("rishmi:", countRishmi)
        # return pluse(countRishmi),countNoRishmi
        count[0] = pluse(count[0])
    elif choose == 2:
        # countNoRishmi = countNoRishmi+1
        chooseing[i] = nameDict[i][1]
        # return countRishmi,pluse(countNoRishmi)
        count[1] = pluse(count[1])
    elif choose == 3:
        choise3(nameDict, chooseing, count, leth, i, index)
        chekeInput(nameDict, chooseing, count, leth, i, index)
    else:
        leth.insert(index, i)
        index = index + 1


def openFile():
    '''the function give information on the kind of the types,
    acording to the chossing of the user8'''
    print(":למידע הודות סגנון מסוים הקש כפי שיפורט להלן")
    print("לסגנון מנתח-1,לסגנון מקדם-2,לסגנון תומך-3,לסגנון משימתי 4")
    print("לסיון הגריפלוג הקש-0")
    num = input()
    num = costToInt(num)

    while num != 0:
        while num not in (1, 2, 3, 4):
            print("שגיאה,נסה שוב")
            num = input()
            num = costToInt(num)
        # if num == 0:

        if num == 1:
            with open("file1.txt", 'r', encoding='utf-8') as f:
                print(f.read())
        elif num == 2:
            with open("file2.txt", 'r', encoding='utf-8') as f:
                print(f.read())
        elif num==3:
            with open("file3.txt", 'r',encoding='utf-8') as f:
                print(f.read())
        else:
            with open("file4.txt", 'r',encoding='utf-8') as f:
                print(f.read())
        print(":למידע הודות סגנון מסוים הקש כפי שיפורט להלן")
        print("לסגנון מנתח-1,לסגנון מקדם-2,לסגנון תומך-3,לסגנון משימתי 4")
        print("לסיון הגריפלוג הקש-0")
        num = input()
        num = costToInt(num)
    print("השאלון הסתיים בהצלחה")

def choise3(nameDict, chooseing, count, leth, i, index):
    '''the function cheke if do you whent to change answer or not'''
    dictShew = {k: v for k, v in chooseing.items() if k < i}
    print(dictShew)
    print("לאישור הקש:1,לשינוי תשובה לאפשרות השנייה,או לשאלה שעדין לא ענית הקש :2,")
    submit = input()
    submit = costToInt(submit)
    while submit != 1 and submit != 2:
        print("תשובה שגויה,נסה שוב:")
        submit = input()
        submit = costToInt(submit)
    if submit == 2:
        chengeAnsowr(nameDict, chooseing, count, leth, index)
