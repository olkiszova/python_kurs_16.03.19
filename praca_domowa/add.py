def add (*args):
    print(args)
    #określamy wymiary potrzebne dla f range

    dims = set()


    for m in args:
        len_rows, len_cols = len(m), len(m[0])
        dims.add ((len_rows, len_cols))
        len_cols_ = set()
        for row in m:
            len_cols_.add(len(row))

        if len(len_cols_)> 1:
            raise ValueError ('liczba kolumn w wierszach jest różna')
        if len(dims) > 1:
            raise ValueError('Wymiary macierzy się nie zgadzają')


    output = []

    for i in range (len_rows):
        row = []
        #print (i, m1[i],m2[i])
        for j in range (len_cols):
           # print (f'i={i}, j={j}, el z m1={m1[i][j]}, el z m2={m2[i][j]}')
           suma = sum([m[i][j] for m in args])
           row.append(suma)
        output.append(row)
    return (output)


m3 = [[1,2], [3,4]]
m4 = [[5,6], [7,8]]

add (m3,m4)