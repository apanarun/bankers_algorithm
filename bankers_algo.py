'''
m=no of process
n=no of resources
process matrix (m)
resource matrix (n)
allocation matrix (n*m)
max matrix (n*m)
available (n)

need (n*m) = max-avaailable
'''
#INPUT DATA
'''
5
P0 P1 P2 P3 P4
3
A B C
0 1 0
2 0 0
3 0 2
2 1 1
0 0 2
7 5 3
3 2 2
9 0 2
2 2 2
4 3 3
3 3 2
'''
#EXPECTED OUTPUT
'''
Safe sequence is ...
['P1', 'P3', 'P4', 'P0', 'P2']
'''

#INPUT DATA
'''
5
P0 P1 P2 P3 P4
3
A B C
0 0 1
1 0 0
1 3 5
0 6 3
0 0 1
0 0 1
1 7 5
2 3 5
1 6 5
5 6 5
1 5 2
'''
#EXPECTED OUTPUT
'''
Safe sequence is not possible
These process can't be executed ...
['P4']
'''


#Input Section
m=int(input())
process_matrix=input().strip().split()
n=int(input())
resource_matrix=input().strip().split()
allocation_matrix=[list(map(int,input().strip().split())) for i in range(m)]
max_matrix=[list(map(int,input().strip().split())) for i in range(m)]
available_matrix=list(map(int,input().strip().split()))
need_matrix=[[max_matrix[i][j]-allocation_matrix[i][j] for j in range(n)] for i in range(m)]
#Funcion to check whether safe sequence is possible or not
def can_be_exec():
    '''
        If any value in need matrix is greater than
        the sum of resource instances of a particular type
        in available and allocation matrix

        Then the process can't be executed
    '''
    cant_be_exec=[]
    flag_out=1
    for i in range(n):
        check=0
        for j in range(m):
            check+=allocation_matrix[j][i]
        check+=available_matrix[i]
        flag=1
        for k in range(m):
            if(max_matrix[k][i]>check):
                flag=0
                cant_be_exec.append(process_matrix[k])
                break
        if(flag==0):
            flag_out=0
    if flag_out:
        return cant_be_exec,1
    else:
        return cant_be_exec,0
cant_be_exec,check=can_be_exec()
if(check==0):
    print("Safe sequence is not possible\nThese process can't be executed ...")
    print(cant_be_exec)
else:
    safe_seq=[]
    while(check and len(safe_seq)<m):
        for i in range(len(need_matrix)):
            if process_matrix[i] not in safe_seq:
                flag=1
                for z in range(n):
                    if(need_matrix[i][z]>available_matrix[z]):
                        flag=0
                if flag:
                    for z in range(n):
                        available_matrix[z]+=allocation_matrix[i][z]
                    safe_seq.append(process_matrix[i])
    print("Safe sequence is ...")
    print(safe_seq)
