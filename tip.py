'''

--For dollars_to_float--

Define a function with name dollars_to_float
accept a param 'd' as a string
replace 'GHC' in 'd' with empty space ' '
then strip off the white space from 'd'
Now convert the 'd' string to float and return it


--For percent_to_float--

Define a function with name percent_to_float
accept a param 'p' as a string
replace '%' in 'p' with empty space ' '
strip of white space from 'p'.
convert the remaining string to float
divide it by 100 and return it


'''


def main():

    cedis = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = cedis * percent
    print(f"Leave GHC{tip:.2f}")
    

def dollars_to_float(d):
    return float(d.replace('GHC', '').strip())
    
def percent_to_float(p):
    return float(p.replace('%', '').strip()) / 100
    
        
main()

