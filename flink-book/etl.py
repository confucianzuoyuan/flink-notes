with open("flink-tutorial.tex", "rt") as fin:
    with open("out.tex", "wt") as fout:
        for line in fin:
            if line.startswith('### '):
                newline = '\section{' + line.split()[1] + '}\n'
                fout.write(newline)
            else:
                fout.write(line)