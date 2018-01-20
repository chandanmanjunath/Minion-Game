def minion_game(string):
    # your code goes here
    def count_overlapping(string,sub):
        count = start = 0
        while True:
            start = string.find(sub, start) + 1
            if start > 0:
                count+=1
            else:
                return count
    def isVowel(char):

        if str(char).lower() == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            return True
        else :
            return False

    #str_var="BAANANAS"
    str_var=string

    list_var=list(str_var)

    score_stuart=0
    score_kevin=0
    letter_count=0
    test_list=[]

    for i in range(0,len(list_var)):
        for j in range(0,len(list_var)):
            if i+j+1 <= len(list_var):
                str_var_temp=''.join(list_var[j:i+j+1])
                if  isVowel(str_var_temp[0]) :
                    if str_var_temp not in test_list:
                        letter_count =count_overlapping(str_var,str_var_temp)
                        score_kevin+=letter_count
                        test_list.append(str_var_temp)

                else:
                    if str_var_temp not in test_list:
                        #letter_count=str_var.count(str_var_temp)
                        letter_count =count_overlapping(str_var,str_var_temp)
                        score_stuart+=letter_count
                        test_list.append(str_var_temp)

    if score_stuart > score_kevin :
        print ('Stuart '+str(score_stuart))
    elif score_kevin > score_stuart:
        print ('Kevin '+str(score_kevin))
    else :
        print ('Draw')
