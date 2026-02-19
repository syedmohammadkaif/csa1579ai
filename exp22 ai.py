bird(ostrich, cannot_fly).
bird(penguin, cannot_fly).
bird(kiwi, cannot_fly).
bird(eagle, can_fly).
bird(pigeon, can_fly).
bird(sparrow, can_fly).
 can_fly(Bird):-
    bird(Bird, can_fly).
