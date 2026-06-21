(defvar p1 '(6 148 72 35 0 33.6 0.627 50))
(defvar p2 '(1 85 66 29 0 26.6 0.351 31))

(defun euclidean-distance (a b)
  (let ((sum 0))
    (dotimes (i 8)
      (let ((diff (- (nth i a) (nth i b))))
        (setq sum (+ sum (* diff diff)))))
    (sqrt sum)))

(format t "Euclidean Distance: ~f~%" (euclidean-distance p1 p2))
