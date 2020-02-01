
def getPizza(fname):
    '''
    param
    - fname: (str) the file name of some data
    output
    - target: (int) the target specified by the question
    - num_type: (int) the number of types of pizza available
    - pizzas: (list) the list of pizzas in slices 
    '''
    fh = open(fname,'r')
    if fh.mode == 'r':
        lines = fh.readlines()
    fh.close()
    line1 = lines[0]
    target, num_type = line1.split()
    target,num_type = int(target),int(num_type)
    pizzas=[]
    for line in lines[1:]:
        for i in line.split():
            pizzas.append(int(i))
    return (target,num_type,pizzas)


def stupidWay(target,pizzas):
    '''
    params
    - target: (int) number of slices required
    - pizzas: (list) list of different pizzas represented by the number of slices each has
    output:
    - sum_so_far: (int) a number of slices smaller or equal to the target, not maximum possible slices
    - records: (list) list of indexs of the pizzas taken
    logic:
    - add slices from the smallest pizza until the sum exceeds the target
    '''
    records = []
    sum_so_far = 0
    for idx,val in enumerate(pizzas):
        if val+sum_so_far>target:
            break
        records.append(idx)
        sum_so_far+=val

    return (sum_so_far, records)

def makeOrder():
    '''
    Calls the function
    '''
    target,num_type,pizzas = getPizza('a_example.in')
    # getPizza('b_small.in')
    # getPizza('c_medium.in')
    # getPizza('d_quite_big.in')
    # getPizza('e_also_big.in')
    print(stupidWay(target,pizzas))
    
if __name__ == "__main__":
    makeOrder()