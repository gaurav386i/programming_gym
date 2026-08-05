## Grammar

# Sepcial words 
    #include int maybe_unused char void double for return

# Punctuation
    {…}, (…), […], [[…]], /*…*/, and <…>.

# Literals
    Our program contains several items that refer to fixed values that are 
    part of the program:
    0, 1, 3, 4, 5, 9.0, 2.9, 3.E+25, .00007, and "element %zu is %g, square is %g"

# Identifiers 
    Identifiers are “names” that we (or the C standard) give to certain 
    entities in the program. 
    Here we have A, i, main, printf, size_t, and EXIT_SUCCESS

# Functions

# Operators 
    Of the numerous C operators, our program only uses a few:

    = : for initializationC and assignmentC
    < : for comparison
    ++: to increment a variable (to increase its value by 1)
    * : to multiply two values

# Attributes 
    Attributes such as [[ maybe_unused ]] are 
    placed into double square brackets as shown and 
    provide some supplemental information to the principle 
    structure of the program.2


# Declarations
    Before we may use a particular identifier in a program, we have to give the compiler a declaration that specifies what that identifier is supposed to represent. In this way, identifiers differ from keywords: keywords are predefined by the language and must not be declared or redefined.

# Statements

    The second part of the main function consists primarily of statements .
    Statements are instructions that tell the compiler what to do with 
    identifiers that have been declared so far