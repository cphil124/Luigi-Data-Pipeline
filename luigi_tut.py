import luigi

class PrintNumbers(luigi.Task):
    n=luigi.IntParameter()

    def requires(self):
        return [] # First Task in the pipeline, so no requirements

    def output(self):
        return luigi.LocalTarget(f'numbers_up_to_{self.n}.txt')
    
    def run(self):
        with self.output().open('w') as f:
            for i in range(1, self.n+1):
                f.write('{}\n'.format())


class SquaredNumbers(luigi.Task):

    n = luigi.IntParameter()

    def requires(self):
        return [PrintNumbers(n=self.n)]
    
    def output(self):
        return luigi.LocalTarget(f'squares_up_to_{self.n}.txt')

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write(f'{n}:{out}\n')

if __name__ == '__main__':
    luigi.run()