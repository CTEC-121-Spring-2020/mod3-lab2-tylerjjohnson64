def function1():
    print(__name__)
    print("\nfunction 1")

def unittest():
    print("unit tests")
    function1()
if __name__ =="__main__":
    unittest()