# def div(x,y):
#     z = x / y
#     return z
#     print(z)
# div(6,3)
# div(3,0)

def div(x,y):
    try:
        z = x / y

    except Exception as e:
        print(z)
        print(e)
div(6,3)
div(3,0)