import time

class StringBuilder:
    def __init__(self):
        self.list = []

    def append(self, val):
        self.list.append(val)

    def __str__(self):
        final_str = ""
        for word in self.list:
            final_str += word
        return final_str

start_time = time.time()
str_builder = StringBuilder()
for i in range(1000):
    str_builder.append('hello')
    str_builder.append('world')
    str_builder.append('By Sai!')

print(str(str_builder))
end_time = time.time()
print(f'This took {end_time - start_time} seconds\n====================================')

start_time = time.time()
s = ""
for i in range(1000):
    for w in ['hello', 'world!', 'By Sai!']:
        s += w
end_time = time.time()
print(f"This took {end_time - start_time} seconds!\n===========================================")

#LLLL, My stringbuilder implementation is slower than python's inbuilt string addition.