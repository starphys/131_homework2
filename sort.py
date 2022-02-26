def sort_list(input_list) :
    i = 0
    while(i < len(input_list)) :
        j = 0
        while(j < len(input_list)-i-1) :
            if(input_list[j] > input_list[j+1]) :
                temp = input_list[j+1]
                input_list[j+1] = input_list[j]
                input_list[j] = temp
            j += 1
        i += 1
    return input_list