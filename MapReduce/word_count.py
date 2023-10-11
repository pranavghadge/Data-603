from mrjob.job import MRJob
import re

class WordCount(MRJob):

    def mapper(self, _, line):
        words = re.findall(r'\w+', line.lower())
        for word in words:
            yield word, 1

    def combiner(self, word, counts):
        yield word, sum(counts)

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()
