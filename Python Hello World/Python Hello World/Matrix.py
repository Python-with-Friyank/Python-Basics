matrixVariable = [['aa',[[8,9,0],9,0],3],[4,5,6],[7,8,9]]
for items in matrixVariable:
    for item in items:
        if(type(item) == list):
            for item1 in item:
                print("> "+ str(item1))
        else:
            print(item)



