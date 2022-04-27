
def pri_num(sel_num: int)->bool:
        result_list = [i for i in range(1, sel_num + 1) if sel_num % i == 0]
        # result = len(result_list) == 2
        # if result == True:
        return len(result_list) == 2        
        



def run():
    pri_num(int(input("selecciona un numero: ")))
    if pri_num == True:
        print("Es un numero primo")
    else:    
        print("no es un numero primo.")



if __name__ == "__main__":
    run()