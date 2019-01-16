#!/usr/bin/env python3
import shutil
append = '''<script type="text/x-mathjax-config">
MathJax.Hub.Config({
	displayAlign: "left"
});
</script>


'''

def conv(ifile, ofile):
    ifile = 'real-src/' + ifile
    ofile = 'src/' + ofile
    with open(ifile, 'r') as inp: 
        with open('/tmp/convwork.md', 'w') as out: 
            out.write(append)
            flag = True 
            pre = '' 
            text = inp.read() 
            for c in text: 
                if pre == '$': 
                    if c == '$': 
                        if flag: 
                            out.write('<div class="math">') 
                        else: 
                            out.write('</div>') 
                        c = '' 
                    else: 
                        if flag: 
                            out.write(r'\\(') 
                        else: 
                            out.write(r'\\)') 
                    flag = not flag 
                elif pre == "\\" and c == "\\":
                    out.write('\\\\\\\\')
                    c = ''
                else: 
                    out.write(pre) 
                pre = c 
            out.write(pre)
    shutil.move('/tmp/convwork.md', ofile)

ma = [
#    ('qf-k.md', 'qf-ko.md'),
#    ('qf-p.md', 'qf-po.md'),
    ('ci-m.md', 'ci-mo.md')
]

if __name__ == '__main__':
    for ifile, ofile in ma:
        conv(ifile, ofile)
