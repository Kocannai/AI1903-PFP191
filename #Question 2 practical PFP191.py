#Question 2
def index(array):
    n=len(array)
    for i in range(n):
        Tong_ben_trai=sum(array[:i])
        Tong_ben_phai=sum(array[i+1:])
        if Tong_ben_trai==Tong_ben_phai:
            return i
    return 0
def main():
    try:
        Array=list(map(int, input('Nhap vao 1 day so: ').split()))
        result=index(Array)
        if result != 0:
            print('Yes')
        else:
            print('No')
    except ValueError:
        print('Error')
if __name__=='__main__':
    main()
