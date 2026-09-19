import re
import sympy as sp
positive_infinity = float('inf')
negative_infinity = float('-inf')
# by multiping the -1 to the target equation we can get max with same algorithm...**
#input = input("enter the equations , separated by | ")
#input_target1 = input(" if its maximazition then enter max :")
input_target1 = 'min'
#input_target2 = ("enter the values:")
#input_target2 = ' -3x2 + -2x1 '
#input_target2 = ' x1 + x2 + -4x3 '
input_target2 = '-2x1  +x2 -x3' # CX values.
#input = " 2x3 + 4x2 <= 5 | 3x2 + 5x3 <= 6 "
#input = " x1 + x2 + 2x3 <= 9 | x1 + x2 + -x3 <= 2 | -x1 + x2 + x3 <= 4 "


input = 'x1 +x2 +x3 == 6 | -x1 +2x2 -0x3 <=4'
input_var_sign = ['pos','pos','neg'] # pos = positive , neg = negative 

equation = input.split('|')

for i in equation: # finding the indexing of X , meaning what is last I in Xi. we do this by finding the len of each equation and capture the biggest .
    pattern_coeff2 = r'([-]?[a-zA-Z0-9]+)'
    a = re.findall(pattern_coeff2,i)
    # print(a,'pattern capture')
    bigest_len = 0
    if len(a[0]) > bigest_len:
        bigest_len = len(a[0])
copy_big_len = bigest_len + 1
print(f'indexing end with X{bigest_len} , i =',bigest_len)
print('input' , input, 'target ',input_target2,'sign ', input_target1)

def fix_equation(key,equation,equation_keys_exist):# this fixes the equation when we have == and want to change to >= or <= , changes all equations for added valess with coeff 0
    for j,i in enumerate(equation):
        # print(i)
        if '<=' in i and b != i:
            i = i.replace('<=','+0'+key+'<=')
            equation[j] = i
            print(equation)
        elif '>=' in i and b != i:
            i = i.replace('>=','+0'+key+' >=')
            equation[j] = i
            print(equation)
        else :
            if b != i:
                i = i.replace('==','+0'+key+'==')
                equation[j] = i
                print(equation)
added_index = 0
if input_target1.upper() == 'MIN':
        m = 0
        n = bigest_len + 1
        for i in equation:
            b = i
            if '<=' in i :
                for p in i.split('<=') :
                    if len(p)>1:
                        pattern_coeff2 = r'([-+]?[a-zA-Z0-9]+)'
                        a = re.findall(pattern_coeff2,p)
                        print(a)
                        for j in a:
                            print(j)
                            print(m)
                            if j[0] == '-' :
                                j1 = j.replace('-','+')
                                b = b.replace(j,j1)
                                print(b)
                                equation[m] = b
                            else:
                                j1 = j.replace('+','-')
                                b = b.replace(j, j1)
                                print (b,'here555')
                                equation[m] = b
                    if len (p) < 2 :
                        pattern_coeff2 = r'([-+]?[a-zA-Z0-9]+)'
                        a = re.findall(pattern_coeff2,p)
                        print(a[0],'heeeeeeeeeeeeeeeereeeeeeee')
                        b = b.replace('<='+a[0],'>='+ '-'+a[0])
                        print(b)
                        equation[m] = b
                m = m + 1
               
            elif '==' in i:
                key = f'x{n}'
                b = b.replace('==',f'+ {key} '+ '>=')
                print(b)
                equation[m] = b
                n = n + 1
                print(equation[m],'here1')
                m = m + 1 
                fix_equation(key,equation,b)
                added_index = added_index + 1
            else:
                m = m + 1 
        # print(m)
pattern_coeff2 = r'([-]?[a-zA-Z0-9]+)'
# print(re.findall(pattern_coeff2,input_target2),'0')
# print(equation)
if input_target1.upper() == 'MAX':
        m = 0
        n = bigest_len + 1
        for i in equation:
            b = i
            if '>=' in i :
                for p in i.split('>=') :
                    if len(p)>1:
                        pattern_coeff2 = r'([-+]?[a-zA-Z0-9]+)'
                        a = re.findall(pattern_coeff2,p)
                        print(a)
                        for j in a:
                            print(j)
                            print(m)
                            if j[0] == '-' :
                                j1 = j.replace('-','+')
                                b = b.replace(j,j1)
                                print(b)
                                equation[m] = b
                            else:
                                j1 = j.replace('+','-')
                                b = b.replace(j, j1)
                                print (b,'here555')
                                equation[m] = b
                    if len (p) < 2 :
                        pattern_coeff2 = r'([-+]?[a-zA-Z0-9]+)'
                        a = re.findall(pattern_coeff2,p)
                        print(a[0],'heeeeeeeeeeeeeeeereeeeeeee')
                        b = b.replace('>='+a[0],'<='+ '-'+a[0])
                        print(b)
                        equation[m] = b
                m = m + 1
            elif '==' in i:
                print(i)
                key = f'x{n}'
                b = b.replace('==',f'-{key} ' +'<=')
                # print(b)
                equation[m] = b
                n = n + 1
                # print(equation[m],'here2')
                m = m + 1 
                fix_equation(key,equation,b)
                added_index = added_index + 1
            else:
                m = m + 1 

# print(equation)
# fixing the target max value :
equation_target = input_target2 # CX VALUES .

if input_target1.upper() == 'MAX':
    pattern_coeff2 = r'([-]?[a-zA-Z0-9]+)'
    a = re.findall(pattern_coeff2,input_target2)
    b = input_target2
    input_target1 = "MIN"
    for i in a:
        if i[0] == '-' :
            i1 = i.replace('-','')
            b = b.replace(i,i1)
            # print (b,'positive')
        else:
            b = b.replace(i, '-'+i)
            # print (b,'negative')
        equation_target = b
        m = m + 1
for j , i in enumerate(equation):# chaning the the value base on the sign , user input , no Free values , cant handle
    pattern_coeff2 = r'([-]?[a-zA-Z0-9]+)'
    a = re.findall(pattern_coeff2,i)
    # print(a , 'removing the minus')
    for e , s in zip(a,input_var_sign):
        # print(e,s)
        if s == 'neg':
            # print(e[0])
            if e[0]=='-':
                p = e.replace(e[0],'')
                i = i.replace(e,p)
                equation[j] = i
                # print(i)
            else:
                i = i.replace(e,'-'+e)
                equation[j] = i
                # print(i)

print("Changes we made , equation , target_min or max , target function ",equation , ' : ',input_target1 , " :",equation_target)

equation = '|'.join(equation)
print(equation)
equation = equation.split('|')# fixes the shape of list for algorithm to read , example ['x1 + x2 + 3x3' , ' -6 ']
print('Ready equation:',equation)
B = []
equation_comp = []
equation_temp = []

for i in equation:
    if '<=' in i:
        equation_comp.append(i.split('<='))
    elif '>=' in i:
        equation_comp.append(i.split('>='))
    else:
        equation_comp.append(i.split('='))

print(equation_comp,'here')
#print("print equation comp :",equation_comp)
for i in range (len(equation_comp)):
    temp = equation_comp[i]
    j = 0
    B.append(int(temp[1])) 
    equation_temp.append(temp[0])
#print(B)
patern_coeff = r'([-]?\d*)x'
patern_coeff1 = r'([a-zA-Z]+[0-9]*)'
#patern_coeff = r'([+-]?\d+)([a-zA-Z0-9]+)'
# finding coeff of equations Xi
coeff_dic_equations = {}
print(equation_temp,'1111111111111111111111')
for i in equation_temp : 
    temp_eq = re.findall(patern_coeff,i)
    temp_eq1 = re.findall(patern_coeff1,i)
    print(temp_eq,temp_eq1)
    for value , key in zip(temp_eq,temp_eq1): # creates the coeff of Xi equations , with using patern and finding the coeffs . 
        #finding the coeff of Xi :
        if value == '' :
            if key in coeff_dic_equations:
                coeff_dic_equations[key].append(1)
            else :
                coeff_dic_equations[key] = [int(1)]
        elif value == '-' :
            if key in coeff_dic_equations:
                coeff_dic_equations[key].append(int(-1))
            else :
                coeff_dic_equations[key] = [int(-1)]
        else:
            if key in coeff_dic_equations:
                coeff_dic_equations[key].append(int(value))
            else:
                coeff_dic_equations[key] = [int(value)]
#find coeffs of C , target .
#print(coeff_dic_equations)
dic_coeffc = {}
coef_C_patern = re.findall(patern_coeff,input_target2)
temp_eq1 = re.findall(patern_coeff1,equation_temp[0])
#print(coef_C_patern)
#print(temp_eq1)
for value , key in zip(coef_C_patern,temp_eq1):
    print(value,key)
    #finding the coeff of Xi for C_list:
    if value == '' :
        dic_coeffc[key] = int(1)
    elif value == '-' :
        dic_coeffc[key] = int(-1)
    else:
        dic_coeffc[key] = int(value)
#print("coeff c",dic_coeffc)
#sorting dics
coeff_dic_equations = {key : coeff_dic_equations[key] for key in sorted(coeff_dic_equations) }
coef_X = coeff_dic_equations.copy()
print(coef_X)
#print(coeff_dic_equations.items())
dic_coeffc = {key :dic_coeffc[key] for key in sorted (dic_coeffc)}
#print(dic_coeffc)
C = []
a = input_target1.upper()
for i , v in dic_coeffc.items() : # checking for target object if its max then its -z minimazing meaning -(-C) = C
                            # this is making the Zj - Cj only , we will make C list after this with this .
    if a == 'MAX' :
        C.append(int(v))
    else :
         C.append(int(-v))
# creating slack variables :
for i in range (len(equation)):
    a = len(equation)
    j = str(i+1)
    key = f'M{j}'
    #print("coeff _ values : ", key)
    value = [0]*a
    value[i] = 1
    coeff_dic_equations[key] = value
    C.append(int(0))
print(added_index)
for i in range(added_index):
    C.append(int(0))
print("-----------------------")
print("*****************************************")
print("the equations variables and coeffs : ",coeff_dic_equations)
C_coeff_values = []
for i in C:
    C_coeff_values.append(i * -1)
print("The main equation:",equation,input_target1)
print("the Value of coeffs of target : ",C_coeff_values)
print("the value of right most of inequality (known as b list ):",B)
print("the Zj - Cj list :",C)
print("C_coeffitients : ",C_coeff_values)
sorted_key1 = [key for key in coeff_dic_equations]
print("sorted list of variables : ",sorted_key1)

#---------------------------
def checkpositive(lista):#true for all positive 
    flag = True
    for i in lista:
        if int(i) >= 0:
            continue
        else: 
            flag = False
            return False
    if (flag != False) :
        return flag
#-----------------------------------
def checknegative (list): # true for all negative 
    flag = True
    for i in list:
        if int(i) <= 0:
            continue
        else: 
            flag = False
            return False
    if (flag != False) :
        return flag
#----------------------- 
#------------------------------------
def find_c_index (dic_list_1 , key):
    for Kelid in dic_list_1.items():
        i = 0 
        if Kelid == key :
            return i
        else : i = i + 1 
#-------------------------------------
def check_min_index(list):
    index_min = 0
    value_min = list[0]
    for index , value in enumerate(list):
        if value == 'inf' or value == '-inf' or value == 0:
            continue
        else:
            if value < value_min :
                value_min = value
                index_min = index
    return index_min
#-------------------------------------
def find_most_positive (list):
    value_inner = 0
    index_inner = 0
    for index , value in enumerate(list):
        if (value <= 0) :
            continue
        else :
            if(value > value_inner):
                value_inner = value
                index_inner = index
    return index_inner


def Simplex_Min(dic_equations ,list_C,list_b,sorted_key_listEQ):
    Basis_list = []
    for i in range (len(equation)+1,len(sorted_key_listEQ)): # base variables  , need to assign once 
        a = sorted_key_listEQ[i]
        Basis_list.append(a)
    k = 1 
    z = 0
    while True :
        #print(Basis_list)
        #step 1 : checking the stop condition :
        print('----------------------------------------------------------------------------')
        print(f'step : {k}')
        print("the Zj - Cj list :",list_C)
        print("the basis list so far : ",Basis_list)
        print("the equations items : ",dic_equations.items())
        print("the b List : ",list_b)
        flag_blist = False
        for i in list_b:
            if int(i)<0:
                print('not fesiable ')
                flag_blist = True
                break
        if flag_blist:
            break
        if (checknegative(list_C)): # false if any element is positive  ,true for every element negative or zero 
            j = 0
            if not(checkpositive(list_b)):
                print(" this is not feasiable :")
                break
            for i in Basis_list: #prints result 
                if (j < len(list_b)):
                    p = list_b[j]
                    print(f'the basis Xi : {i} :the value :{p} ')    
                    j = j + 1 
            print("the value of Z : ",z)
            break
        enter_variable_index = find_most_positive(list_C) # a = index of variable that enters
        enter_variable = sorted_key_listEQ[int(enter_variable_index)] # variable that enters
        print("the variable that enters : ",enter_variable)
        flag = checknegative(dic_equations[enter_variable]) # unbounded feasible solution 
        if flag == True :
            j = 0 
            print('bounded but infinite :')
            for i in Basis_list:
                if j < len(list_b):   
                    p = list_b[j]
                    print(f'the basis Xi : {i}:the value :{p} ')
                    j = j + 1
            break
        # finding pivot :
        pivot = []
        pivot_choice_list = dic_equations[enter_variable]
        for i in range (len(pivot_choice_list)):
            if i < len(list_b):
                # checking division dividing 
                if (pivot_choice_list[i] < 0) : # if yk is negative , dont try 
                    pivot.append('inf')
                    continue
                elif (pivot_choice_list[i] > 0) :
                    pivot.append(float('{:.3f}'.format(list_b[i]/pivot_choice_list[i])))
                else:
                    pivot.append(positive_infinity)
                i = i + 1
        print(f'step {k} : pivot list :{pivot_choice_list}')
        #select min pivot :
        Min_value_index = check_min_index(pivot)
        #chaning the names of basis variable :
        Basis_list[Min_value_index] = enter_variable
        # fixing variable for doing operations
        variable = sorted_key_listEQ[enter_variable_index]
        value_to_div = dic_equations[variable][Min_value_index]
        f = 0
         # dividing by value of min index for making 1 in pivot slot
        for key in dic_equations.keys():
            if(dic_equations[key][enter_variable_index] != 0):
                dic_equations[key][enter_variable_index] = float('{:.5f}'.format(dic_equations[key][enter_variable_index] / value_to_div))
            if (f < len(list_b) and f == enter_variable_index):
                list_b[f] = float('{:.5f}'.format(list_b[f] / value_to_div))
                f = f + 1 
        # 0 above and below coloum , effects C_list and certain index of Xi and Mi 
        temp_value = dic_equations[enter_variable]
        #finding value for making 0 in rows :
        X = sp.symbols('x') # min_value_index = index of row that we are making 0 using it 
        value_substitute = 0
        m = 0
        for i in range (len(temp_value)):
            if i == enter_variable_index :
                continue
            else:# finding rows , and checking the row is not same row as pivot  and doing operations 
                    value_0 = temp_value[enter_variable_index]
                    value_1 = dic_equations[enter_variable][i]
                    EQU = sp.Eq(value_0 * X + value_1,0)
                    value_substitute = float(sp.solve(EQU,X)[0])
                    value_substitute = float('{:.5f}'.format(value_substitute))
                    for j in dic_equations.keys():
                        temp = dic_equations[j][enter_variable_index]
                        temp2 = float('{:.5f}'.format(temp * value_substitute))
                        dic_equations[j][i] = dic_equations[j][i] + float(temp2)
                        #chaning B_list values : 
                    if i < len(list_b):
                        temp_3 = list_b[enter_variable_index] * value_substitute
                        list_b[i] = list_b[i] + temp_3 
        # chaning c_list :
        y = sp.symbols('y')
        # selecting Ci with using the index of Xi
        c_value  = list_C [enter_variable_index]
        y_coeff = temp_value[enter_variable_index]
        EQU1 = sp.Eq(y_coeff*y + c_value,0)
        value_substitute_1 = float('{:.5f}'.format(sp.solve(EQU1,y)[0]))
        i = 0
        for key in dic_equations.keys():
            temp = float('{:.5f}'.format(dic_equations[key][enter_variable_index] *value_substitute_1 ))
            list_C[i] = float('{:.5f}'.format(list_C[i] + temp))
            i = i + 1
        z = z + (list_b[enter_variable_index] * value_substitute_1) # finding value of Z with table 
        # changing C values 
        #returns and checks the conditions to stop 
        i = 0
        j = 0
        p = 0
        k = k + 1
# decide what to do , 
Simplex_Min(coeff_dic_equations,C,B,sorted_key1)