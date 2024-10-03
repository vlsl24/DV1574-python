dict1={'a': 1, 'b': 2}
dict2={'b': 3, 'c': 4}

def merge_dicts(dict1, dict2):
    dict3={}
    for i in dict1:
        if i not in dict2:
            dict3[i]=dict1[i]
    
    for i in dict2:
        if i not in dict3:
            dict3[i]=dict2[i]
        
        else:
            dict3[i]=dict2[i]   
    return dict3             
                     