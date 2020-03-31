
def gaus1(n, m):
    # Прямой ход
    for i in range(0,n-1):
        q = m[i][i] # коэффициент, диагональный элемент
        for j in range(0,n+1):
            m[i][j] = m[i][j] / q  # преобразование ведущей строки 
        for k in range(i+1,n):
            q2 = m[k][i] # второй коэффициент
            for j in range(i,n+1):
                m[k][j] = m[k][j] - m[i][j] * q2 # преобразование ведомой строки
    ans = [0 for i in range(n)]
    # print(m)
    
    # Обратный ход
    ans[n-1] = m[n-1][n]/m[n-1][n-1]
    for i in range(n-1,-1,-1): 
        summa = 0
        for j in range(i+1,n):
            summa += m[i][j]*ans[j]
        ans[i] = (m[i][n] - summa) / m[i][i]
    return ans   
        
def gaus2(n, m):
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

# n колво строк, 
def main():
    """
    n = int(input("Введите размер матрицы "))
    print("Введите матрицу")
    
    matrix = []
    
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        matrix.append(row)
    """
    matr2 = [[5,7,6,5,23],[7,10,8,7,32],[6,8,10,9,33],[5,7,9,10,31]]
    print("Ответ 1:")
    print(gaus1(4,matr2))
    print("Ответ 2:")
    matr3 = [[5,7,6,5,23],[7,10,8,7,32],[6,8,10,9,33],[5,7,9,10,31]]
    print(gaus2(4,matr3))
    pass

main()
