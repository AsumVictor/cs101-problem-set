def main():
    # Accept input from user and convert to integer and store as mass
    mass = int(input('Enter the mass in KG: '))
    
    # Convert mass to
    energy = convertEnergy(mass)
    # print the converted energy
    print(f'{energy} Joules ')
    
 # Define a function to handle conversion
def convertEnergy(mass):
    # Accept integer mass as a parameter
    # Same he constand value of speed of light as C
    C = 300000000
    # Convert to energy by multiplying mass by C square
    energy_joule = mass * (C**2)
    
    # Return Energy
    return energy_joule 
    
    
    
main()

