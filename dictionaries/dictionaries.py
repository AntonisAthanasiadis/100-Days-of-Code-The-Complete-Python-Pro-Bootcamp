programming_terms = {
    "Variable": "A container for storing data values.",
    "Function": "A reusable block of code that performs a specific task.",
    "Loop": "A way to repeat a block of code multiple times.",
    "Boolean": "A data type that can only be True or False."
}

def get_definition(term):
    #print(programming_terms[term]) alternative way, crashes on unknown term
    definition = programming_terms.get(term, "Term not found in dictionary.")
    print(f"{term}: {definition}")

get_definition("Variable")
get_definition("Loop")
get_definition("Algorithm")