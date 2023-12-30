def minion_game(string):
    kev=0
    stu=0
    vowels="AEIOU"
    leng=len(string)
    for i in range(leng):
            if string[i] in vowels:
                 kev+=leng-i
            else:
                 stu+=leng-i
    if kev==stu:
        print("Draw")
    elif kev>stu:
        print("Kevin", kev)
    else:
        print("Stuart", stu)
            

if __name__ == '__main__':
    s = input()
    minion_game(s)