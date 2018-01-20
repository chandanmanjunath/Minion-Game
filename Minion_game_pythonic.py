def minion_game(string):
    # your code goes here
    score_kevin,score_stuart=0,0
    str_length=len(string)
    for idx,sub in enumerate(s):
        if sub in 'AEIOU':
            score_kevin+=str_length-idx
        else:
            score_stuart+=str_length-idx

    if score_stuart > score_kevin :
        print ('Stuart '+str(score_stuart))
    elif score_kevin > score_stuart:
        print ('Kevin '+str(score_kevin))
    else :
        print ('Draw')
