(define (split-at lst n)
	(cond 
		((= n 0)
			(cons nil lst)
			)
		((null? (cdr (split-at lst (- n 1)))) 
			(cons lst nil))
		(else 
			(cons 
				(append 
					(car (split-at lst (- n 1)))
				 	(list (car (cdr (split-at lst (- n 1)))))
				 	) 
		  	 	(cdr (cdr (split-at lst (- n 1)))) 
				)
			)
		)	
	)                           

(define (compose-all funcs) 
	(cond
		((null? funcs) (lambda (x) (+ x 0)))
		(else 
			(lambda (x) 
				((compose-all (cdr funcs)) ((car funcs) x))
				)
			)
		)
	)
