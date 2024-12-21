import random

def Slot_Machine():
    symbol = ["%","@","#","$","&","~"]
    option = [random.choice(symbol) for _ in range(3)]
    
    print("-------")
    print(f" | {option[0]} | | {option[1]} | | {option[2]} |")
    print("-------")
    
    if option[0] == option[1] == option [2]:
        print("Congratulation.... You Won!!!!")
    
    else :
        print("Oopss.... You Lost!!!!")
        
        
        
if __name__ == "__main__":
    Slot_Machine()