import time
import pandas as pd

from collections import Counter
from razdel import tokenize
from tqdm import tqdm

cheesy = pd.read_csv("cheesy.csv")
titles_dict = Counter()

t1 = time.time()
for title in tqdm(cheesy["title"]):
    time.sleep(0.025)
    tokens = [_.text for _ in list(tokenize(title.lower()))]
    titles_dict.update(Counter(tokens))
t2 = time.time()

print(titles_dict.most_common(10))
print(t2-t1)
