from array_stack_work import ArrayStack


def is_matched(expr):
    """Return True if all delimiters are properly match; False otherwise."""
    lefty = '({['  # opening delimiters
    righty = ')}]'  # respective closing delims

    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)  # push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False  # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False  # mismatched
    return S.is_empty()  # were all symbols matched?


example1="[(5+x)-(y+z)]"
example2="()(()){([()])}"
example3=")(()){([()])}"
example4="({[])}"
another="( { [5*3 ] +2) -1}"

if is_matched(example1):
    print("The equation is balanced")
else:
    print("The equation is not balanced")

if is_matched(example2):
    print("The equation is balanced")
else:
    print("The equation is not balanced")
if is_matched(example3):
    print("The equation is balanced")
else:
    print("The equation is not balanced")

if is_matched(example4):
    print("The equation is balanced")
else:
    print("The equation is not balanced")

if is_matched(another):

    print("The equation is balanced")
else:
    print("The equation is not balanced")
