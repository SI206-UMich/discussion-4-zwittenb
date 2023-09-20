#Zach 
class Rectangle():
    # Create the constructor "__init__" method
    # Arguments: width (an ingeter), height (an integer)
    # 
    # It sets an instance variable, "width" to the passed argument, width
    # It sets an instance variable, "height" to the passed argument, height

    # YOUR CODE HERE

    def __init__(self,width,height):
        self.width = width
        self.height = height

    # Create the "__str__" method
    #
    # It returns a string, 
    #       "A rectangle with width ____ and height ____"
    def __str__(self):
        return "A rectangle with width " + str(self.width) + " and height " + str(self.height)

    # YOUR CODE HERE



    # Create the "verify_input" method
    #
    # It returns a boolean
    #       True if the width and height are positive numbers
    #       False otherwise

    # YOUR CODE HERE
    def verfity_input(self):
        if self.width > 0 and self.height > 0:
            return True
        else:
            return False


    # Create the "area" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the area of the rectangle.

    # YOUR CODE HERE

    def area(self):
        if self.height > 0 and self.width > 0:
            return self.width * self.height
        else:
            return "invalid output"
        

    # Create the "perimeter" method
    #
    # It first verifies inputs and return "Invalid input" if they are invalid.
    # Otherwise, it returns the perimeter of the rectangle.

    # YOUR CODE HERE
    def perimeter(self):
        perimeter = 2* (self.width + self.height)
        return perimeter



def main():
    r = Rectangle(10, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

    r = Rectangle(0, 10)
    print(r)
    print("Area:", r.area())
    print("Perimeter:", r.perimeter())
    print()

if __name__ == "__main__":
    main()