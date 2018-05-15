import re
from functools import reduce

def sum(x,y):
    return x + y

def mult(x,y):
    return x * y

class Buffer():
    def __init__(self,buffer=[],operator=sum):
        self.buffer = buffer
        self.operator = operator

    def add(self,el):
        self.buffer.append(el)

    def reduce(self):
        init = 0 if self.operator is sum else 1
        return reduce(self.operator,self.buffer,init)

def iter_helper(tokens):
    buffer_stack = [Buffer([])]
    for token in tokens:
        cur_buffer = buffer_stack[len(buffer_stack) - 1]
        if token is '(':
            prev_buffer = cur_buffer
            cur_buffer = Buffer([])
            buffer_stack.append(cur_buffer)
        elif token is ')':
            val = cur_buffer.reduce()
            buffer_stack.pop()
            prev_buffer = buffer_stack[len(buffer_stack) - 1]
            prev_buffer.add(val)
        elif token is '*':
            cur_buffer.operator = mult
        elif token is '+':
            cur_buffer.operator = sum
        else:
            cur_buffer.add(int(token))
    cur_buffer = buffer_stack[len(buffer_stack) - 1]
    return cur_buffer.reduce()




def tokenize(s):
    """
    Given an S-expression string consisting of non-negative integers and operators (+,*,-,/), return the tokens of the string.
    """
    return re.split('\s+', re.sub('\s+|(?=[-*+/()])', ' ', s).strip())

def evaluate(s):
    """
    Given an S-expression consisting of non-negative integers and operators (+,*), evaluate the string.
    """
    return iter_helper(tokenize(s))

test_data = [
        ('3', 3),
        ('(+ 1 2)', 3),
        ('(* 2 3)', 6),
        ('(* 2 (+ 5 3))', 16),
        ('(+ 1 2 3)', 6),
        ('(+)', 0),
        ('(*)', 1),
        ('(* (* 10 2) (+ 5 7 (+)) (*) (+ 105 (+ 1 3)))', 26160),
        ]

tests = 0
for expression,output in test_data:
    tests += 1
    result = evaluate(expression)
    assert result == output, ("Failed test evaluate('%s') = %s, which is not %s" % (expression, result, output))

print("\nDone. %s assertions." % tests)
