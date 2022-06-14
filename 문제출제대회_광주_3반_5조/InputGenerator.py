import random
input_file = open("C:/Users/최영선/Desktop/ssafy/sample_input.txt",'w',encoding='utf-8')
input_file.write('50' + '\n')
for tc in range(50):
    N = random.randrange(5, 101)
    arr_four = range(N, N*2)
    arr_wall = range(N, N*2)
    number_four = random.choice(arr_four)
    number_wall = random.choice(arr_wall)
    arr = ['0'] * (N ** 2 - (3 + number_four + number_wall))
    arr.extend(['1','2','3'])
    arr.extend(['4'] * number_four)
    arr.extend(['-1'] * number_wall)
    arr = random.sample(arr, N**2)
    input_file.write(str(N) + '\n')
    for i in range(N):
        input_file.write(' '.join(arr[i*N:i*N+N])+'\n')
