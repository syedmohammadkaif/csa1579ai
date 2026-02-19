% define some facts about birds and their properties
bird(ostrich, cannot_fly).
bird(penguin, cannot_fly).
bird(kiwi, cannot_fly).
bird(eagle, can_fly).
bird(pigeon, can_fly).
bird(sparrow, can_fly).

% define a predicate to check if a bird can fly
can_fly(Bird) :-
bird(Bird, can_fly).

% example queries
?- can_fly(eagle).
true.

?- can_fly(ostrich).
false.

?- bird(Bird, cannot_fly).
Bird = ostrich ;
Bird = penguin ;
Bird = kiwi.
?- bird(Bird, can_fly).
Bird = eagle ;
Bird = pigeon ;
Bird = sparrow.
