


def func(arr, list_tuples):
    t = len(list_tuples)
    print("t:", t)
    print('\n')

    for elem in list_tuples:
        print(elem)
        l = elem[0]
        r = elem[1]
        print(f"l:{l}, r:{r}")

        for i in range(l,r+1):
            arr[i] = arr[i] + 100
        print(arr)
        print('\n')

    print("maximum elem:", max(arr))
    

func([10,10,10,10,10], [(1,3), (0,2)])



