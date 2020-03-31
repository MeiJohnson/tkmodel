def solve(n,m):
     # Прямой ход
    for i in range(0,n-1):
        q = m[i][i] # РЭ, диагональный элемент
        m[i][i] = 1
        for j in range(0,n+1):
            m[i][j] = m[i][j] / q  # преобразование ведущей строки 
        for k in range(i+1,n):
            q2 = m[k][i] # запоминаем коэф
            for l in range(n+1):
                m[k][l] = m[k][j] - m[i][j] * q2 # преобразование ведомой строки
    ans = [0 for i in range(n)]
    print(m)
    
    # Обратный ход
    ans[n-1] = m[n-1][n]/m[n-1][n-1]
    for i in range(n-1,-1,-1): 
        summa = 0
        for j in range(i+1,n):
            summa += m[i][j]*ans[j]
        ans[i] = (m[i][n] - summa) / m[i][i]
    return ans   
    


def main():
    matr = [[5,7,6,5,23],[7,10,8,7,32],[6,8,10,9,33],[5,7,9,10,31]]
    print(solve(4,matr))
    pass

main()