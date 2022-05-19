import re

#input file
fin = open("index.md", "rt")
#output file to write the result to
fout = open("newindex.md", "wt")
#for each line in the input file
figcount = 0
for line in fin:
  m = re.match(r'!\[(.*)\]\((.*)\)', line)
  if m:
    figcount += 1
    s = '<figure><img src="{figpath}" alt="{figname}" style="width:100%"><figcaption>图-{figcount} {figname}</figcaption></figure>'.format(figname=m.group(1),figpath=m.group(2),figcount=figcount)
    fout.write(s)
  else:
    #read replace the string and write to output file
    fout.write(line)
#close input and output files
fin.close()
fout.close()
