def main():
    plate = input('Plate:  ')
    
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')
    
    
def is_valid(s):
    # check for lenth 
    if not 2<= len(s) <= 6:
        return False
    
    
    
main()