def binary_search(list , target ):
    start , middle , steps , end = 0 , 0 , 0 , len(list)

    while(start<=end):
        print(f"Step {steps} : {list[start: end+1 ]}")
        steps =steps+1
        middle =(start+end)//2

        if target== list[middle]:
            return middle
        if target <list[middle]:
            end = middle-1
        else :
            start =middle +1
    return -1




list = [1,2,3,4,5,6,7,8,9]
target = 9

binary_search(list,target)

