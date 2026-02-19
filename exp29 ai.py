student(ravi).
studies(ravi).
pass(X):-
    student(X),
    studies(X).
happy(X):-
    pass(X).
