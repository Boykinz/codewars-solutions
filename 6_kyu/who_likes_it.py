def likes(a):

    if len(a) >= 4:
        return a[0] + ", " + a[1] + " and " + str(len(a)-2) + " others like this"

    elif len(a) == 3:
        return a[0] + ", " + a[1]  + " and " + a[2] + " like this"
    
    elif len(a) == 2:
        return a[0] + " and " + a[1] + " like this"

    elif len(a) == 1:
        return a[0] + " likes this" 
        
    else:
        return "no one likes this"