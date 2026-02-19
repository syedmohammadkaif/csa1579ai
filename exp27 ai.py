% Graph
edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(e,f).

% Heuristic (small value = best)
h(b,4).
h(c,2).
h(d,6).
h(e,1).
h(f,0).   % Goal

% Best First Search
bestfs(Node, Goal) :-
    Node = Goal.

bestfs(Node, Goal) :-
    findall(X, edge(Node,X), Children),
    choose(Children, Best),
    bestfs(Best, Goal).
% Graph
edge(a,b).
edge(a,c).
edge(b,d).
edge(c,e).
edge(e,f).

% Heuristic values (smaller is better)
h(a,5).
h(b,4).
h(c,2).
h(d,6).
h(e,1).
h(f,0).   % Goal node

% Best First Search
best_first(Start, Goal, Path) :-
    bfs([Start], Goal, [Start], Path).

bfs(Goal, Goal, Visited, Visited).

bfs(Current, Goal, Visited, Path) :-
    findall(Next,
           (edge(Current,Next),
            \+ member(Next,Visited)),
           Children),
    choose_best(Children, Best),
    bfs(Best, Goal, [Best|Visited], Path).

choose_best([H], H).
choose_best([H1,H2|T], Best) :-
    h(H1,V1), h(H2,V2),
    (V1 < V2 ->
        choose_best([H1|T], Best)
    ;
        choose_best([H2|T], Best)
    ).

choose([X], X).
choose([X,Y|T], Best) :-
    h(X,H1), h(Y,H2),
    (H1 < H2 -> choose([X|T], Best)
               ; choose([Y|T], Best)).
