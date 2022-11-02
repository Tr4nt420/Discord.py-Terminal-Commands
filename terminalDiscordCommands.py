import aioconsole


listOfCommands = {}
async def start(loop):
    loop.create_task(get_input())

def terminalCommand(func):
    listOfCommands[func.__name__] = func
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner
async def get_input():
    while True:
        i = await aioconsole.ainput(">")
        i = i.strip()
        chars_ =[]
        isQuoteMet = False 
        isBracketMet = False
        str_ = ""
        for index, c in enumerate(i):
            if not c in "[]":
                str_ += c
            l = []
            if (c == " " and not isQuoteMet) or len(i)-1==index:
                if isBracketMet:
                    for i in str_.split(","):
                        l.append(i.strip().strip('"'))
                    isBracketMet = False
                else:
                    chars_.append(str_.strip('"').strip())
                str_ = ""


            elif c == '"':
                if not isQuoteMet:
                    isQuoteMet = True
                else:
                    isQuoteMet = False
                    if isBracketMet:
                        for i in str_.split(","):
                            l.append(i.strip().strip('"'))
                    else:
                        chars_.append(str_.strip('"').strip())
                    isBracketMet = False
                    str_ = ""
            elif c in "[":
                if not isBracketMet:
                    isBracketMet = True
                else:
                    isBracketMet = False
            chars_.append(l)

        chars_ = [i for i in chars_ if i]
        args = []
        dict_ = {}
        for v in chars_[1:]:
            if isinstance(v, str):
                args.append(v)
                if v.startswith("-"):
                    dict_[v[1:]] = True
            else:
                args.append(v)
        if len(dict_) > 0:
            args.append(dict_)
            for i in dict_:
                args.remove("-"+i)
        args = [i.strip('"').strip() if isinstance(i, str) else i for i in args]
        args = [i for i in args if i]

        if chars_[0] in listOfCommands:
            try:
                res = await listOfCommands[chars_[0]](*args)
                if isinstance(res, bool):
                    print("Command succesfully executed")
                else:
                    print(res)
            except Exception as e:
                print("Error from command: ", e)

        else:
            print("Unknown command: ", chars_[0])
