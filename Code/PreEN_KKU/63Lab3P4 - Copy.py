"""
Write a function leaky_relu to take 2 arguments:
(1) a list of primary input values and
(2) a leaky factor (as a floating-point number).
"""

def leaky_relu(x, a):
  if x >= 0:
    y = x
  else:
    y = x*a
  return y


#ข้างล่างนี้ห้ามแก้
if __name__ == '__main__':

    r = leaky_relu(-10, 0.005)
    print(r)

    r = leaky_relu(-10, 0.05)
    print(r)

    r = leaky_relu(-2, 0.05)
    print(r)

    r = leaky_relu(0, 0.05)
    print(r)

    r = leaky_relu(2, 0.05)
    print(r)

    r = leaky_relu(10, 0.05)
    print(r)