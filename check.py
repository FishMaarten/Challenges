import re
from os import listdir
from os.path import abspath, join
from typing import List

abs_path = abspath("./Collection/")
names = ["alber","chirag","hedia","kristof","maarten","robin","saba","santosh","seppe","steven","tomas","wim"]
names = [f".*{name}.*" for name in names]
challenges = {d:[f for f in listdir(join(abs_path, d)) for name in names if re.match(name, f)] for d in listdir(abs_path)}

for k,v in challenges.items():
    if len(v) > 1: print(f"{len(v)} in {k}: " + str([re.sub("[^A-z]","",name)for name in names if re.match(name, str(v))]))
