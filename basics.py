counter = 0  #стартовое значение couter!!
for _ in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1  #прибавка +n к стартовому значению

print('Было введено', counter, 'чисел, больших 10.')
