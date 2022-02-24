import random
import time

def nask(amin = 20, amax = 1000):
    q = True
    while q == True:
        try:
            a = int(input('Введите число от 20 до 1000: '))
            if a < amin:
                print('Получено число меньше 20. Попробуйте снова.')
            elif a > amax:
                print('Получено число больше 1000. Попробуйте снова.')
            else:
                break
        except:
            print('Неверный ввод данных, попробуйте снова.')
    nlist = [random.randint(1000, 99999) for i in range(a)]
    op1 = time.process_time()
    bub_sort(nlist)
    op = time.process_time() - op1
    return a, op, nlist,

def bub_sort(nlist):
    p = nlist
    h = len(p)
    for i in range(h):
        for j in range(h - i - 1):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
    
def main():
    s = nask()
    print(f'-------------------------------------------------------')
    print(f'Количество чисел в списке: {s[0]}')
    print(f'Процессорное время, затраченное на сортировку: {s[1]:0.3f} сек.')
    print(f'Сумма 10 минимальных чисел: {sum(s[2][:10])}')
    print(f'Сумма 10 максимальных чисел: {sum(s[2][-10:])}')
    
main()