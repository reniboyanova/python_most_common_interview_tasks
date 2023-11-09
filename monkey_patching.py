class SomeClass:
    def original_method(self):
        return "Original method"

# Monkey patching to modify the behavior of the original method
def new_method(self):
    return "Patched method"

SomeClass.original_method = new_method

obj = SomeClass()
print(obj.original_method())  # This will call the monkey-patched method
