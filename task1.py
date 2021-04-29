def task1():
    n = input("Enter Your Input: ")
    arr = ['A' , 'B' , 'C', 'D', 'E', 'F' , 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T' , 'U', 'V', 'W', 'X', 'Y', 'Z']
    arr_n = list(n)
    arr_total = len(arr)
    result = 0 
    res_arr=arr_n[::-1]
    if n.strip().isdigit():
        n_to_number = int(n)
        result = ''
        print(n_to_number)
        while n_to_number > 26:
            total = divmod(n_to_number , 26) 
            if total[1] == 0 :
                result = result  + 'Z'
                n_to_number = total[0] - 1
            elif total[1] != 0:
                result = result + arr[total[1] - 1]
                n_to_number = total[0]
            if total[0] <= 26 and total[1] != 0:
                print(abs(total[1] - 2))
                result = result + arr[abs(total[0] - 1) ]
            elif total[0] < 26 and total[1] == 0:
                result = result + arr[abs(total[0] - 2) ]    
        print(result[::-1])
    else :
        for i in range(len(n)):
            if i == 0:
                result = arr.index(res_arr[i]) + 1
            else:
                result = result + ((arr_total ** i)  * (arr.index(res_arr[i]) + 1))
        print(result)


task1()         