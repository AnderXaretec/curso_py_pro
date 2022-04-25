
def pri_num(sel_num: int)->bool:
        result_list = [i for i in range(1, sel_num + 1) if sel_num % i == 0]
        result = len(result_list) == 2
        if result == True:
            print("El ", sel_num, "Es un numero primo")
        else:
            print("El ", sel_num, " no es un numero primo. Estos son sus divisores:\n ", result_list)    
        



def run():
    pri_num(int(input("selecciona un numero: ")))











if __name__ == "__main__":
    run()