import math 
def polar_to_cartesian(r,theta):
# convert polar coordinates (r, theta) to cartesiam coordinates (x,y)
    def polar_to_cartesian(r, theta):
        theta_rad = math.radians(theta)

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return(round(x, 5), round(y, 5)) 

r = float(input("Enter r"))
theta = float(input("Enter theta"))

print(polar_to_cartesian(r, theta))




# convert cartesian coordinates (x,y) to polar coordinates (r,theta)
def cartesian_to_polar(x,y):

    r = math.sqrt(x**2) + (y**2)
    theta = math.atan(y / x)

    return(round(r, 5), round(theta, 5))

x = float(input("Enter x"))
y = float(input("Enter y"))

print(cartesian_to_polar(x,y))



# calculate the position of a pendulum
def pendulum_position(A, T, phi, t):
    omega = 2 * math.pi / T
    phi_rad = math.radians(phi)
    x_t = A * math.cos(omega * t + phi_rad)
    return(round (x_t,5)) 

A = float(input("Enter A"))
T = float(input("Enter T"))
phi = float(input("Enter phi")) 
t = float(input("Enter t"))

print(pendulum_position(A, T, phi, t))

