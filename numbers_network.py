from sklearn.linear_model.perceptron import Perceptron
from numbers_mass import one, two
import itertools
from generate_picture import read_image
x = [list(itertools.chain.from_iterable(one)), list(itertools.chain.from_iterable(two))]
print(x)
y = [1, 2]

clf = Perceptron(random_state=241)
clf.fit(x, y)


if __name__ == "__main__":
       print(clf.predict([list(itertools.chain.from_iterable(one)),]))
       print(clf.predict([list(itertools.chain.from_iterable(read_image('1.png'))),]))