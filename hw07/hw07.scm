(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (ordered? s)
    (cond 
        ((null? s) #t)
        ((null? (cdr s)) #t)
        (else 
              (if (> (car s) (car (cdr s)))
                #f
                (ordered? (cdr s))
                )
            )
        )
    )

(define (square x) (* x x))

(define (pow base exp)
    (cond 
        ((= exp 1) base)
        ((= exp 0) 1)
        ((= (modulo exp 2) 0) (square (pow base (quotient exp 2))) )
        ((= (modulo exp 2) 1) (* base (square (pow base (quotient exp 2)))))
        )
    )
