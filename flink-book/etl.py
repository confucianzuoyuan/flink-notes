with open("flink-tutorial.tex", "rt") as fin:
    with open("out.tex", "wt") as fout:
        for line in fin:
            if line.startswith('![](images'):
                newline = '\\begin{figure}[htbp]\n\centering\n\includegraphics[width=0.6\\textwidth]{' + line.split('![](')[1][:-2] + '}\n\end{figure}\n'
                fout.write(newline)
            else:
                fout.write(line)