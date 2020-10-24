from mrjob.job import MRJob
from mrjob.step import MRStep


class RatingsBreakdown(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_ratings,
                   reducer=self.reducer_count_ratings)
        ]

    'Wichtig: Einbinden der Datei unter Run --> Edit Configurations'
    def mapper_get_ratings(self, _, line):
        (user_id, movie_id, rating, timestamp) = line.split('\t')
        yield rating, 1

    def reducer_count_ratings(self, movie_id, count):
        yield movie_id, sum(count)

if __name__ == '__main__':
    RatingsBreakdown.run()
