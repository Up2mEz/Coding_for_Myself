''' math '''
def f_func(x):
    """ f_function """
    f_ans = 7*(x**2)+3*x+11
    return f_ans

def g_func(x,y):
    """ g_function """
    g_upper = (3*(f_func(x)))**0.5
    g_lower = 4*y
    g_ans = (g_upper/g_lower)-5*x*y
    return g_ans

def h_func(x,y,z):
    """ h_func """
    h_upper = g_func(((f_func(z**2))+x**y),g_func(x*y,f_func(g_func(y,((z**5)**0.5)))))
    h_lower = (2*x*((z*(y**2))**0.5))+91
    h_outer = ((7*x*y)/(13*z))+6
    h_ans = (h_upper/h_lower)+h_outer
    return h_ans

def main():
    """ main """
    x = float(input())
    y = float(input())
    z = float(input())
    answer_h = h_func(x,y,z)
    answer_g = g_func(x,y)
    answer_f = f_func(x)
    print(f"{answer_h:.3f}\n{answer_g:.3f}\n{answer_f:.3f}")
main()
