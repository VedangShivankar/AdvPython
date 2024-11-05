'''class Accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print("user define exception:", self.msg)


try:
    raise Accident('car crash')
except Accident as e:
    e.print_exception() 
'''
#section 2

def process_file():
    try:
        f = open("C:\\Vedang\\Software\\PythonCodes\\advpython\\data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside")
    finally:
        print("cleaning up file")
        f.close()
 
process_file()