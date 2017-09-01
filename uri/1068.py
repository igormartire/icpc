try:
    while True:
        expression = input()
        openCnt = 0
        correct = True
        for c in expression:
            if c == '(':
                openCnt += 1
            elif c == ')':
                if openCnt == 0:
                    correct = False
                    break
                openCnt -= 1
        if openCnt > 0:
            correct = False
        print("correct" if correct else "incorrect")
except EOFError:
    pass