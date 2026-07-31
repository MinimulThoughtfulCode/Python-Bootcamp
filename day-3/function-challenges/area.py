#Area of Triangle
#Takes the base and height and returns the area

def triangle(b, h):
  #Calculates the area of the square
  answer = (b * h) / 2
  return answer

#Takes user input
base = int(input("What is the base: "))
height = int(input("What is the height: "))

#Finds the area
area = triangle(base, height)
print("The area is: ", area)
