parent(liz, jim).

% Mother relation
mother(X, Y) :-
female(X),
parent(X, Y).

% Father relation
father(X, Y) :-
male(X),
parent(X, Y).

% Grandmother relation
grandmother(X, Y) :-
female(X),
parent(X, Z),
parent(Z, Y).

% Grandfather relation
grandfather(X, Y) :-
male(X),
parent(X, Z),
parent(Z, Y).

% Sister relation
sister(X, Y) :-
female(X),
parent(Z, X),
    parent(liz, jim).

% Mother relation
mother(X, Y) :-
female(X),
parent(X, Y).

% Father relation
father(X, Y) :-
male(X),
parent(X, Y).

% Grandmother relation
grandmother(X, Y) :-
female(X),
parent(X, Z),
parent(Z, Y).

% Grandfather relation
grandfather(X, Y) :-
male(X),
parent(X, Z),
parent(Z, Y).

% Sister relation
sister(X, Y) :-
female(X),
parent(Z, X),
    parent(liz, jim).

% Mother relation
mother(X, Y) :-
female(X),
parent(X, Y).

% Father relation
father(X, Y) :-
male(X),
parent(X, Y).

% Grandmother relation
grandmother(X, Y) :-
female(X),
parent(X, Z),
parent(Z, Y).

% Grandfather relation
grandfather(X, Y) :-
male(X),
parent(X, Z),
parent(Z, Y).

% Sister relation
sister(X, Y) :-
female(X),
parent(Z, X),
