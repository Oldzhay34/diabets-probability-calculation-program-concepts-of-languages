p1([6, 148, 72, 35, 0, 33.6, 0.627, 50]).
p2([1, 85, 66, 29, 0, 26.6, 0.351, 31]).

sum_squares([], [], 0).
sum_squares([H1|T1], [H2|T2], Sum) :-
    sum_squares(T1, T2, Rest),
    Diff is H1 - H2,
    Sum is Rest + Diff * Diff.

:- initialization(main).

main :-
    p1(P1), p2(P2),
    sum_squares(P1, P2, Sum),
    Dist is sqrt(Sum),
    format("Euclidean Distance: ~f~n", [Dist]),
    halt.