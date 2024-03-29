
def set_matrix_zero(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    dummy_row = [-1]*rows
    dummy_column = [-1]*columns

    for i in range(rows):
        for j in range(columns):
            if matrix[i][j]==0:
                dummy_row[i]=0
                dummy_column[j]=0


    for i in range(rows):
        for j in range(columns):
            if dummy_row[i] == 0 or dummy_column[j] == 0:
                matrix[i][j] = 0

    return matrix


def main():
    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
    ans = set_matrix_zero(matrix)
    print(ans)

if __name__ == '__main__':
    main()
