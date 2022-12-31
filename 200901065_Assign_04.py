import threading 

  

class InputThread(threading.Thread): 

    def __init__(self): 

        super().__init__() 

        self.string = None 

     

    def run(self): 

        try: 

            self.string = input("Enter String In Small Letters (Input Thread): ") 

        except Exception as e: 

            print("Invalid String !!", e) 

  

class ReverseThread(threading.Thread): 

    def __init__(self, input_thread): 

        super().__init__() 

        self.input_thread = input_thread 

     

    def run(self): 

        self.input_thread.join() 

        print("Reversed Thread Output: ", self.input_thread.string[::-1]) 

  

class CapitalThread(threading.Thread): 

    def __init__(self, input_thread): 

        super().__init__() 

        self.input_thread = input_thread 

     

    def run(self): 

        self.input_thread.join() 

        print("Capitalized Thread Output:", self.input_thread.string.upper()) 

  

class ShiftThread(threading.Thread): 

    def __init__(self, input_thread): 

        super().__init__() 

        self.input_thread = input_thread 

     

    def run(self): 

        self.input_thread.join() 

        shifted_string = "" 

        for c in self.input_thread.string: 

            shifted_string += chr(ord(c) + 2) 

        print("Shifted Thread Output:", shifted_string) 

  

input_thread = InputThread() 

reverse_thread = ReverseThread(input_thread) 

capital_thread = CapitalThread(input_thread) 

shift_thread = ShiftThread(input_thread) 

  

input_thread.start() 

reverse_thread.start() 

capital_thread.start() 

shift_thread.start()
