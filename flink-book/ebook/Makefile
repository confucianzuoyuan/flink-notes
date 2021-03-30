html:
	pandoc -s --toc --mathjax -c pandoc.css flink-tutorial.md -o output.html

epub:
	rm -rf output.epub
	pandoc --toc --mathjax -o output.epub flink-tutorial.md

docx:
	cp flink-tutorial.md flink-tutorial-docx.md
	gsed -i 's/svg/png/g' flink-tutorial-docx.md
	pandoc -o output.docx flink-tutorial-docx.md
	rm -rf flink-tutorial-docx.md

pdf:
	cp flink-tutorial.md flink-tutorial-pdf.md
	gsed -i 's/svg/pdf/g' flink-tutorial-pdf.md
	pandoc flink-tutorial-pdf.md -o output.tex --template=./template.tex --pdf-engine=xelatex --top-level-division=chapter --from markdown+implicit_figures
	rm -rf flink-tutorial-pdf.md
	xelatex output.tex
	xelatex output.tex
	rm -rf *.log
	rm -rf *.aux
	rm -rf *.toc

clean:
	rm -rf *.log
	rm -rf *.aux
	rm -rf *.toc