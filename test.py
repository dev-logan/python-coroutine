def hello(name):
    def printer():
        print(f"Hello {name}!")

    return printer


func = hello("Fox")
func()
