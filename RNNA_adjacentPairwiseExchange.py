from numpy  import *
from TSP_data import * 
#-------------------------------------------------------------------------------------------------------------------------------
Expense = (['Ottawa',inf,353,422,283,369,294,228,154,259,212,314,466,1314,583],
['Edmonton',336,inf,211,232,395,444,407,324,406,349,197,261,1529,216],
['Victoria',384,195,inf,267,427,473,438,353,441,400,232,245,1577,253],
['Winnipeg',270,226,278,inf,296,359,316,254,309,281,184,314,1464,270],
['Fredericton',221,409,461,313,inf,275,207,221,354,226,353,490,1500,415],
['St. Johns',275,473,522,387,287,inf,200,317,282,357,445,767,1583,480],
['Halifax',212,440,492,341,217,198,inf,259,263,264,380,577,1554,449],
['Toronto',145,343,392,273,221,331,255,inf,257,165,307,457,1436,371],
['Charlottetown',248,425,479,335,357,273,255,254,inf,267,373,562,1573,546],
['Quebec City',200,382,459,313,254,363,270,174,272,inf,341,486,1578,500],
['Regina',293,186,237,179,329,403,342,280,340,297,inf,286,1510,244],
['Whitehorse',409,230,230,367,435,463,446,399,443,417,265,inf,1598,276],
['Iqaluit',1197,inf,inf,inf,inf,inf,inf,1308,inf,1410,inf,1610,inf,1757],
['Yellowknife',321,222,237,244,466,419,384,319,535,421,223,276,1634,inf])
def TSP(city_matrix,city=""):
    """
    Description: returns heuristic solution and objective function value when given the corresponding matrix and starting city (optional)
    
    Input:
        city_matrix: a tuple where each element is a list of length n+1. there are n such elements in the tuple
        city: a string (optional: if not specified, an empty string is used instead)
    
    Output:
        prints a string
    """
    
    M = convert_Matrix(city_matrix)
    if is_valid_matrix(M)== False:
       raise ValueError
    feasible_solution = RNNA(M)
    solution_list = convert_string_to_list(feasible_solution[0])
    new_solution = adjacent_pairwise_exchanges(solution_list, M)
    #print new_solution
    rearranged_solution = starting_city(new_solution[0], city)
    city_solution = convert_int_to_City(rearranged_solution)
    city2number = {} 
    print "Heuristic solution:" + str(city_solution)
    print "value of objective function:" + str(objective_function(rearranged_solution,city_matrix))

#-------------------------------------------------------------------------------------------------------------------------------              
def add_city_to_tour(i_row, j, tour):
    """
    Description: Given the row from the cost matrix that represents the current city i (i_row), 
                 the index of the minimum value in i_row (j), and an incomplete feasible solution (tour),
                 the function returns the closest city to city i that is not already in the feasible solution
                 (eliminating subtours)
    Input: 
        i_row: a list
        j: an integer <= (n-1). n is the number of cities
        tour: a list where 1 <= len(tour) <= n
        
    Output:
        returns an integer, where 0 <= output <= (n-1), and output is not in tour
      
    """
    copy_i_row = i_row[:]
    if j not in tour: 
        return j        
    if j in tour:
        copy_i_row[j]=inf
        if min(copy_i_row)==inf:
            return -1
        new_j = copy_i_row.index(min(copy_i_row))
        return add_city_to_tour(copy_i_row, new_j, tour)

def adjacent_pairwise_exchanges(feasible_solution, M):
    """
    Description: switches adjacent pairs of cities in a feasible solution and returns the one with
                 the smallest objective function
    
    Input:
        feasible_solution: a list containing len(M) + 1 integers
        M: a tuple where each element is a list of length n. there are n such elements in the tuple
    
    Output:
        returns a tuple (list, integer)s
        
    """
    current_best = objective_function(feasible_solution, M)
    best_tour = feasible_solution[:]
    for i in range(len(M)-1):
        x = i
        y = i + 1
        new_feasible_solution = switch(x, y, feasible_solution[:-1])
        new_feasible_solution.append(new_feasible_solution[0])
        new_obj_function = objective_function(new_feasible_solution,M)
        if new_obj_function < current_best:
            current_best = new_obj_function
            best_tour = new_feasible_solution[:]
    return best_tour, current_best

def convert_int_to_City(solution):
    """
    Description: converts a list into a string of cities, by accessing global dictionary "city2number"
    
    Input:
        solution: a list of integers 
    
    Output:
        returns a string
    """
    final_solution = ""
    for i in solution:
        final_solution += city2number[i] + "-"
    final_solution = final_solution[:-1]
    return final_solution
    
def convert_list_to_string(tour):
    """
    Description: converts a list into a string where the elements of the list are natural numbers joined together by a '-'
                (sample output: '1-2-3-4-1')
    Input:
        tour: a list containing len(M) + 1 integers
        
    Output:
        returns a string
        
    """
    strtour = []
    for i in tour:
        i += 1
        j = str(i)
        strtour.append(j)
    newstrtour = '-'.join(strtour)
    return newstrtour

city2number = {}

def convert_Matrix(city_m):
    """
    Description: converts a matrix with labels (names of cities) into a matrix containing only numbers.
                 City names and corresponding row/column numbers are stored in a global dictionary "city2number". 
    Input: 
        city_m: a tuple where each element is a list of length n + 1. the first element of each list is a label; the other n elements 
                are integers or floats. there are n such lists in the tuple
                
    Output:
        returns a tuple where each element is a list consisting of n float values. 
    """
    
    global city2number
    k = 0
    for i in city_m:
        city2number[k]= str(i[0])
        del i[0]
        k += 1   
    return city_m

def convert_string_to_list(string):
    """
    Description: takes a string of integers separated by a '-' (e.g. '1-2-3-4-1'), and converts it to a list of ints [1, 2, 3, 4, 1]
    
    Input:
        string: a string of integers separated by a '-'
    
    Output:
        returns a list of integers
        
    """
    strlist = string.split('-')
    intlist = []
    finallist = []
    if len(strlist) == 0:
        return finallist
    for i in strlist:
        intlist.append(int(i))
    for i in intlist:
        i -= 1
        finallist.append(i)
    return finallist

def feasible_solution(i, M, tour):
    """
    Description: Given the current city (i), the cost-matrix (M), and the current incomplete feasible solution (tour),
                 the city, the nearest neighbour to the current city is selected and added to the solution (provided it
                 is not already in the solution. if it is, the next-nearest neighbour is selected). The nearest neighbour
                 then replaces the current city and the process is repeated until there are n cities in the feasible 
                 solution. The procedure then terminates and the feasible solution is returned
    Input:
        i: an integer such that 0 <= i <= (n-1)
        M: a tuple where each element is a list of length n. there are n such elements in the tuple
        tour: a list where 0 <= len(tour) <= n
    
    Output:
        returns a list containing n integers between 0 and n-1
        
    """
    solution = tour
    while len(tour) != len(M):
        i_row = M[i]
        j = i_row.index(min(i_row))
        next_city = add_city_to_tour(i_row, j, solution)
        if next_city == -1:
            return -2
        solution.append(next_city)
        i = next_city
    return solution
    
    
def is_valid_matrix(M):
    """
    Description: Given a matrix, determines if the matrix has an equal number of rows and columns (i.e. is an n x n matrix)

    Input:
        M: a tuple where each element is a list
    
    Output:
        returns a boolean value
    """
    rows = len(M)
    for i in M:
        if len(i) != rows:
            print i
            print "row length " + str(len(i))
            print "matrix length " + str(len(M))
            return False
    return True
       
def minimum_in_dictionary(dictionary):
    """
    Description: returns the key and value of the minimum value entry in a dictionary
    Input:
        dictionary: a dictionary in which the values are integers
        
    Output:
        returns a tuple (string, integer)
        
    """
    min_value = inf
    dictionary_key = ""
    for i in dictionary:
        if dictionary[i] < min_value:
            min_value = dictionary[i]
            dictionary_key = i
    return dictionary_key, min_value
    
def objective_function(tour, M):
    """
    Description: Given the feasible solution (tour), and the cost-matrix, the value of the objective function is
                 returned
    Input:
        tour: a list consisting of len(M) + 1 integers
        M: a tuple where each element is a list of length n. there are n such elements in the tuple
    
    Output: 
       returns an integer 
       
    """
    x = 0
    y = 1
    z = 0
    while x < len(M):
        i = tour[x]
        j = tour[y]
        z += M[i][j]
        x += 1
        y += 1
    return z
    
def RNNA(cost_matrix):
    """
    Description: returns a heuristic solution to the travelling salesman problem when given an input of the 
                 corresponding cost-matrix
    Input: 
        cost_matrix: a tuple where each element is a list of length n. there are n such elements in the tuple
    
    Output:
        returns a string and integer
            
    """
    M = cost_matrix[:]
    tour = []
    all_tour = {}
    for i in range(len(M)):
        starting_city = i
        tour.append(starting_city)
        new_tour = feasible_solution(starting_city, M, tour)
        if new_tour != -2:
            new_tour.append(starting_city)
            string_tour = convert_list_to_string(new_tour)
            z = objective_function(new_tour, M)
            all_tour[string_tour] = z
            tour = [] 
    min_entry = minimum_in_dictionary(all_tour)
    invalid = 0
    for i in all_tour:
        if all_tour[i] ==inf:
            invalid += 1
    if invalid > 0:
        print "Total number of routes searched out of " +str(len(M))+": " + str(len(M) - invalid)
    minimum_z = min_entry[1]
    corresponding_tour = min_entry[0]
    
    return corresponding_tour, minimum_z

def starting_city(solution, city=""):
    """
    Description: Rearranges a feasible solution such that it is starting with the specified city
    
    Input:
        solution: a list of integers
        city: a string (optional: if not specified, an empty string is used instead)
    
    Output:
        returns a list of integers
    """
    if city == "":
        return solution
    index = inf
    for i in city2number:
        if city2number[i] == city:
            index = i
            break
    if index == inf:
        return "No city found"
    k = 0
    for i in solution:
        if i == index:
            del solution[len(solution)-1]
            first_half = solution[:k]
            new = solution[k:]
            new = new + first_half
            new.append(i)
            break
        k += 1
    return new    

def switch(x, y, tour):
    """
    Description: Switch two pairs in a feasible solution (tour).
    
    Input:
        x: an integer between 0 and len(tour) - 1. it is not equal to y
        y: an integer between 1 and len(tour). it is not equal to x 
        tour: a list containing integers/float. the first and last items are identical
    
    Output:
        returns a list in which the first and last items are identical
        
    """
    tour_copy1 = tour[:]
    tour_copy2 = tour[:]
    tour_copy1[x] = tour_copy2[y]
    tour_copy1[y] = tour_copy2[x]
    return tour_copy1
