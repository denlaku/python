# coding=UTF-8
# pylint: disable=invalid-name
'''
StringIO
'''
import pickle
import io

f = io.StringIO()
pickle.dump([1], f)
print(f.getvalue())

if __name__ == "__main__":
    print("--------------------")
