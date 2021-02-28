html:
	asciidoctor flink-tutorial.adoc

epub:
	rm -rf output.epub
	pandoc --toc --mathjax -o output.epub flink-tutorial.md

docx:
	cp flink-tutorial.adoc flink-tutorial-docx.adoc
	sed -i 's/svg/png/g' flink-tutorial-docx.adoc
	asciidoctor --backend docbook --out-file - flink-tutorial-docx.adoc | pandoc --from docbook --to docx --output flink-tutorial.docx --highlight-style espresso
	rm -rf flink-tutorial-docx.adoc

pdf:
	cp flink-tutorial.md flink-tutorial-pdf.md
	sed -i 's/svg/pdf/g' flink-tutorial-pdf.md
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
