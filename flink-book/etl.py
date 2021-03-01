with open("flink-tutorial.tex", "rt") as fin:
    with open("out.tex", "wt") as fout:
        for line in fin:
            if line.startswith('## '):
                newline = '\section{' + line.split()[1] + '}\n'
                fout.write(newline)
            elif line.startswith('### '):
                newline = '\subsection{' + line.split()[1] + '}\n'
                fout.write(newline)
            elif line.startswith('#### '):
                newline = '\subsubsection{' + line.split()[1] + '}\n'
                fout.write(newline)
            elif line.startswith('```java'):
                newline = '\\begin{minted}[linenos,breaklines,fontsize=\\footnotesize]{java}\n'
                fout.write(newline)
            elif line.startswith('```scala'):
                newline = '\\begin{minted}[linenos,breaklines,fontsize=\\footnotesize]{scala}\n'
                fout.write(newline)
            elif line.startswith('```xml'):
                newline = '\\begin{minted}[linenos,breaklines,fontsize=\\footnotesize]{xml}\n'
                fout.write(newline)
            elif line.startswith('```sh'):
                newline = '\\begin{minted}[linenos,breaklines,fontsize=\\footnotesize]{sh}\n'
                fout.write(newline)
            elif line.startswith('```sql'):
                newline = '\\begin{minted}[linenos,breaklines,fontsize=\\footnotesize]{sql}\n'
                fout.write(newline)
            elif line.startswith('```'):
                newline = '\end{minted}\n'
                fout.write(newline)
            elif line.startswith('![](images'):
                newline = '\\begin{figure}[htbp]\n\centering\n\includegraphics[width=0.6\\textwidth]{' + line.split('![](')[1][:-2] + '}\n\end{figure}\n'
                fout.write(newline)
            else:
                fout.write(line)