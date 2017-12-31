# coding=UTF-8
# pylint: disable=invalid-name
'''
pickle
'''
import pickle
# import cpickle

arr = ['apple', 'mango', 'carrot']
str0 = "学习python"
f = open('tmp/pickle_001', "wb")
pickle.dump(arr, f)
f.close()

print(pickle.load(open('tmp/pickle_001', "rb")))

# if __name__ == "__main__":
#     print("--------------------")
