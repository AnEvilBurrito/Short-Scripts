
def linear_search(the_list, target): 
    '''
    Searches through a python list and the index of the target, or -1 if it does not exist in the list 
    '''
    for idx, item in enumerate(the_list): 
        if target == item: 
            return idx 
        
    return -1





if __name__ == "__main__":
    
    data = [5,4,3,2,1]
    
    result = linear_search(data, 1)
    
    print(result)
    
    result2 = linear_search(data, '11')
    
    print(result2)