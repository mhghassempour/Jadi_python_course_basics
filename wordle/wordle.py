with open("words.txt") as f:
    word = f.readlines()

my_word = 'apply'
high_score = 100000000
freq = 'esiarntolcdugpmkhbyfvwzxqj'
words = [w.strip() for w in word]
words = [w.lower() for w in words]

for w in words:
    if len(set(list(w))) == len(w):
        if len(w) != 5:
            continue
        else:
            score = 0

            for c in w:
                score += freq.index(c)

            if score < high_score:
                print(w, score)
                high_score = score

