from mrjob.job import MRJob
from mrjob.step import MRStep
import csv


class MostPopularMovie(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
            # TODO add second reducer here
        ]

    # mapper
    def mapper_get_ratings(self, _, line):
        # TODO add your code here
        pass

    # first reducer
    def reducer_count_ratings(self, key, values):
        # TODO add your code here
        pass

    # second reducer
    def reducer_find_max(self, key, values):
        # TODO add your code here
        pass


if __name__ == '__main__':
    MostPopularMovie.run()
