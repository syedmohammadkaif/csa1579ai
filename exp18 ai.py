teaches(join, math).
teaches(jane, english).
teaches(bob, science).
teaches(sue, history).
teaches(tom, art).

takes(alice, math).
takes(alice, science).
takes(bob, english).
takes(bob, science).
takes(yogi, history).
takes(yogi, art).
takes(deva, math).
takes(deva, english).
takes(deva, art).

teaches_subjects(Teacher, Subjects):-
    teaches(Teacher, Subject).

taking_students(Subject, Student):-
    takes(Student, Subject).
