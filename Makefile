TEXFILE = tmp.tex

main:
	./try.py > $(TEXFILE)
	xelatex $(TEXFILE)

dvi:
	./try.py > $(TEXFILE)
	xelatex -no-pdf $(TEXFILE)

view:
	evince $(TEXFILE:.tex=.pdf)

clean :
	rm -f $(TEXFILE:.tex=*) *~ 


