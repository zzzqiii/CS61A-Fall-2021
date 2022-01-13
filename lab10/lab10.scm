(define (over-or-under num1 num2) (if (< num1 num2) -1 (if (= num1 num2) 0 1)))
(define (over-or-under num1 num2) (cond ((< num1 num2) -1) ((= num1 num2) 0) (else 1)))
(define (make-adder num) (lambda (inc) (+ num inc)))
(define (make-adder num) (define (add_num inc) (+ inc num)) add_num)
(define (composed f g) (lambda (x) (f (g x))))

(define lst (list (cons 1 nil) 2 (list 3 4) 5))
;wrong answer, but don't know why wrong
; (define (remove item lst)
;     (cond
;         ((= lst nil) nil)
;         ((= (cdr lst) nil)
;             (if (= (car lst) item) 
;                 nil 
;                 lst)
;             )
;         (else
;             (if (= (car lst) item) 
;               (remove item (cdr lst)) 
;               (append (list (car lst)) (remove item (cdr lst)))
;                 )
;             )    
;         )
;     )
(define (remove item lst)
    (filter (lambda (x) (not (= x item))) lst)
    )

