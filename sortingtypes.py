def insert_sort(A):
    '''sorting list A by insert'''
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1

def choise_sort(A):
    '''sorting list A by choices'''
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    '''sorting list A by bubble'''
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorithm):

    print('\nTesting', sort_algorithm.__doc__)
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('testcase #2: ', end='')
    A = list(range(10, 40)) + list(range(10))
    A_sorted = list(range(40))
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 3]
    A_sorted = [2, 2, 3, 4, 4]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)