(custom-set-variables
  ;; custom-set-variables was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )
(custom-set-faces
  ;; custom-set-faces was added by Custom.
  ;; If you edit it by hand, you could mess it up, so be careful.
  ;; Your init file should contain only one such instance.
  ;; If there is more than one, they won't work right.
 )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; python-mode ¼³d
;; http://www.emacswiki.org/cgi-bin/wiki/PythonMode
;; python-mode.el
;; emacs /lisp/progmodes 
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(autoload 'python-mode "python-mode" "Python Mode." t)
(add-to-list 'auto-mode-alist '("\\.py\\'" . python-mode))
(add-to-list 'auto-mode-alist '("\\.pyw\\'" . python-mode))
(add-to-list 'interpreter-mode-alist '("python" . python-mode))

(add-hook 'python-mode-hook
(lambda ()
(set (make-variable-buffer-local 'beginning-of-defun-function)
'py-beginning-of-def-or-class)
(setq outline-regexp "def\\|class ")))

#!lisp
;; FIXME emacs에서는 설정파일에 아래처럼 해준다고 해결 될만큼 TAB은 단순한것 같지 않다. :(
(setq default-tab-width 4)

;;굴림체를 기본 글꼴로 지정
;;(setq default-frame-alist ' 
;;	( 
;;		(font . "-*-굴림체-normal-r-*-*-17-*-*-*-c-*-ksc5601-*") 
;;		(height . 45) 
;;		(width . 80) 
;;	) 
;;) 

;;굴림체를 기본 글꼴로 지정
(setq default-frame-alist ' 
	( 
		(font . "-*-굴림체-normal-r-*-*-17-*-*-*-c-*-ksc5601-*") 
		(foreground-color . "white") 
		(background-color . "black") 
		(cursor-color . "white") 
		(height . 45) 
		(width . 80) 
	) 
) 