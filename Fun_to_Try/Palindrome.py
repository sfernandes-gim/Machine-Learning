def check_palin( str_input):
    
    print(str_input)
    # if len(str_input)<=1:
    #     return "Not Palindrome"
    
    # if (str_input == str_input[::-1]):
    #     return "Palindrome"
    # else:
    #     return "Not Palindrome"

    st_pos = 0
    end_pos = len(str_input)-1

    while (st_pos<end_pos):
        if str_input[st_pos]!=str_input[end_pos]:
            return "Not Palindrome"
        st_pos +=1
        end_pos -=1
    
    return "Palindrom"

str1="noalon"

print(check_palin(str1))
        


    