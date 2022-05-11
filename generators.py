import time

def fibo_gen(max):
    n1 = 0
    n2 = 1
    counter = 0
    for i in range(0, max):
        if i == 0:
            yield n1
        elif i == 1:
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            yield aux
    # while True:
    #     if counter == 0:
    #         counter += 1
    #         yield n1
    #     elif counter == 1:
    #         counter += 1
    #         yield n2
    #     else:
    #         aux = n1 + n2
    #         n1, n2 = n2, aux
    #         counter += 1
    #         if counter == max + 1:
    #             raise StopIteration
    #         yield aux

if __name__ == "__main__":
    max = int(input("Cuantos numeros de Fibonacci quieres? "))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)