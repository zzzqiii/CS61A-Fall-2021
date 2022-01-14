(define (my-filter func lst)
    (cond
        ((null? lst) nil)
        ((func (car lst))
               (cons (car lst) (my-filter func (cdr lst))))
        (else
            (my-filter func (cdr lst))
            )
        )
    )

(define (interleave s1 s2)
    (cond
        ((null? s1) s2)
        ((null? s2) s1)
        (else
            (cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2))))
            )
        )
    )

(define (accumulate merger start n term)
    (cond
        ((= n 0) start)
        (else (merger (accumulate merger start (- n 1) term) (term n)))
        )
    )

(define (no-repeats lst)
    (cond
        ((null? lst) nil)
        (else (cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst)))))
        )
    )
