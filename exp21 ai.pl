hanoi(1, Source, Target, _):-
    format('Move disk from Source ~w to Target ~w~n', [Source, Target]).
hanoi(N, Source, Target, Aux) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Aux, Target),
    hanoi(1, Source, Target, _),
    hanoi(N1, Aux, Target, Source).
