def max_elem(k,m,n):
    """Функция поиска максимального элемента"""
    max_el = 0
    for i in range(k,n):
        for j in range(k,n):
            if abs(m[i][j]) > abs(max_el):
                max_el = m[i][j]
                max_i = i
                max_j = j
    max_res = [max_el,max_i,max_j] 
    return max_res

def swapm(m,k,n,max_i,max_j):
    """Функция обмена"""
    for j in range(n+1):
        temp_1 = m[k][j]
    #print(temp_1)
        m[k][j] = m[max_i][j]
    #print(m[k])
        m[max_i][j] = temp_1
    #print(m[max_i])

    for i in range(n):
        temp_2 = m[i][k]
        m[i][k] = m[i][max_j]
        m[i][max_j] = temp_2
   
    temp_index = m[n][k]
    m[n][k] = m[n][max_j]
    m[n][max_j] = temp_index
    print(m)
    return m  
            
    

def method3(n, m):
    for k in range(n-1):
        maxe = max_elem(k,m,n)
        print(maxe)
        m = swapm(m, k, n, maxe[1], maxe[2])
    
    #print(m)                  
    
     # Прямой ход
    for i in range(n-1):
        for k in range(i+1,n):
            q = m[k][i] / m[i][i]
            for j in range(i,n+1):
                m[k][0] = 0
                m[k][j] = m[k][j] - q * m[i][j]
    ans = [0 for i in range(n)]
    #print(m)
    
    # Обратный ход
    ans[n-1] = m[n-1][n]/m[n-1][n-1]
    for i in range(n-1,-1,-1): 
        summa = 0
        for j in range(i+1,n):
            summa += m[i][j]*ans[j]
        ans[i] = (m[i][n] - summa) / m[i][i]
        
    return ans

def main():
    matr = [[5,7,6,5,23],[7,10,8,7,32],[6,8,10,9,33],[5,7,9,10,31],[0,1,2,3]]
    print(method3(4,matr))
    
main()
