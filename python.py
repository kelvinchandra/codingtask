def task(n1, n2):
    arr1 = list(n1)
    arr2 = list(n2)
    result = True
    print(arr1)
    print(arr2)
    for index, value in enumerate(arr1):
        if value == '#':
            del arr1[index-1]

    for index, value in enumerate(arr2):
        if value == '#':
            del arr2[index-1]

    print(' arr1 %s' % "".join(arr1).lower())
    print(' arr2 %s' % "".join(arr2).lower())

    if "".join(arr1).lower() == "".join(arr2).lower():
        print(result)
    else:
        result = False
        print(result)

task("Ab#C", "AC#C")