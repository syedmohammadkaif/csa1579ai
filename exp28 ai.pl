% Symptoms
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).
symptom(fatigue).

% Diseases
disease(flu) :-
% -------- Symptoms --------
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).
symptom(fatigue).
symptom(sore_throat).

% -------- Disease Rules --------

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(headache).

% Facts (Symptoms)

symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).
symptom(body_pain).
symptom(fatigue).
symptom(vomiting).
symptom(diarrhea).

% Rules (Diseases)

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(common_cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sore_throat).

disease(migraine) :-
    symptom(headache),
    symptom(nausea).

disease(food_poisoning) :-
    symptom(vomiting),
    symptom(diarrhea),
    symptom(fever).

% Diagnosis Rule

diagnosis :-
    disease(Disease),
    write('The patient may have: '),
    write(Disease), nl.

diagnosis :-
    write('Disease not identified. Please consult a doctor.'), nl.
disease(common_cold) :-
    symptom(cough),
    symptom(sore_throat).

disease(measles) :-
    symptom(fever),
    symptom(rash).

disease(covid19) :-
    symptom(fever),
    symptom(cough),
    symptom(fatigue).
    symptom(fever),
    symptom(cough),
    symptom(headache).

disease(measles) :-
    symptom(fever),
    symptom(rash).

disease(covid) :-
    symptom(fever),
    symptom(cough),
    symptom(fatigue).
% Facts (Symptoms)

symptom(fever).
symptom(cough).
symptom(headache).
symptom(sore_throat).
symptom(runny_nose).
symptom(body_pain).
symptom(fatigue).
symptom(vomiting).
symptom(diarrhea).

% Rules (Diseases)

disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(body_pain).

disease(common_cold) :-
    symptom(cough),
    symptom(runny_nose),
    symptom(sore_throat).

disease(migraine) :-
    symptom(headache),
    symptom(nausea).

disease(food_poisoning) :-
    symptom(vomiting),
    symptom(diarrhea),
    symptom(fever).

% Diagnosis Rule

diagnosis :-
    disease(Disease),
    write('The patient may have: '),
    write(Disease), nl.

diagnosis :-
    write('Disease not identified. Please consult a doctor.'), nl.
