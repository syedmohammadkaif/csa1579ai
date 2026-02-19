% Facts: fruit and their colors

fruit(apple, red).
fruit(banana, yellow).
fruit(grapes, green).
fruit(mango, yellow).
fruit(orange, orange).
fruit(guava, green).
fruit(pomegranate, red).

% Rule to find fruit by color
find_fruit(Color, Fruit) :-
    fruit(Fruit, Color).
