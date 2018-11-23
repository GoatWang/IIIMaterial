import os
import re

dirs = [d for d in os.listdir() if bool(re.match('\d+\_.+?', d))]
for d in dirs: 
    for f in os.listdir(d):
        if f.startswith('main') and f.endswith('.ipynb'):
            readfile_path = os.path.join(d, f)
            writefile_path = os.path.join(d, f.replace("main", "practice"))
            print(readfile_path)
            print(writefile_path)
            readfile = open(readfile_path, 'r', encoding='utf8')
            writefile = open(writefile_path, 'w', encoding='utf8')
            starts_equal = False
            starts_all = False
            for line in readfile:
                if "#==============your works ends================#" in line:
                    starts_equal = False
                if "#!==============your works ends================!#" in line:
                    starts_all = False
                if starts_equal and "=" in line:
                    line = line.split("=")[0] + "=" + line[-5:]
                if starts_all:
                    line = line[:5] + line[-5:]
                if "#=============your works starts===============#" in line:
                    starts_equal = True
                if "#!=============your works starts===============!#" in line:
                    starts_all = True

                writefile.write(line)
                
            readfile.close()
            writefile.close()
