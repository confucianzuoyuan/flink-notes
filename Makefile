all:
	@echo Making beamer ...
	xelatex -shell-escape slide1.tex
	xelatex -shell-escape slide2.tex
	xelatex -shell-escape slide3.tex
	xelatex -shell-escape slide4.tex
	xelatex -shell-escape slide5.tex
	xelatex -shell-escape slide6.tex
	xelatex -shell-escape slide7.tex

slide3:
	xelatex -shell-escape slide3.tex

slide4:
	xelatex -shell-escape slide4.tex
	
clean:
	@echo Done. 
	-rm -f *.aux
	-rm -f *.bbl *.blg *.log *.out *.ps *.thm *.toc *.toe *.lof *.lot *.nav *.snm *.vrb 
	-rm -f *.loa *.aen
	-rm -f *.html *.css *.scm *.hlog
	-rm -f _region_.tex
	-rm -f -rf auto
	-rm -f *.fen
	-rm -f *.ten
	-rm -f *.bcf
	-rm -f *.pyg
	-rm -f *.xml
	-rm -rf *.prv

