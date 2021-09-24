def namelist(names):
    x = [item['name'] for item in names]
    return (', '.join(x[:-1]) + ' & '*(len(x)>1) 
            + str(x[-1]) if len(x) > 0 else '')