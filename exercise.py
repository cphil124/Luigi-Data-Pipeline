import luigi
import os
import inspect
import sklearn.feature_extraction.text as tfeat
import sklearn.model_selection as ms


class InputText(luigi.ExternalTask):
    filename = luigi.Parameter()

    def output(self):
        """
        Returns target output for this task.
        Returns a Luigi Target Object: :py:class: 'luigi.target.Target'
        """


        # Directory containing this file
        root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/'
        return luigi.LocalTarget(root + self.filename)

class Vectorize(luigi.Task):
    input_dir = luigi.Parameter()
    evaluate = luigi.BoolParameter()

    def requires(self):
        return [ InputText(self.input_dir + '\\' + filename)
                for filename in os.listdir(self.input_dir)]

    def run(self):
        corpus = []
        labels = []

        vectorizer = tfeat.TfidfVectorizer()

        for f in self.input(): # self.input() returns the output for the tasks in requires()
            with f.open('r') as fh:
                labels.append(fh.readline().strip())
                corpus.append(fh.read())
            
        corpus, X_test, labels, y_test = ms.train_test_split(corpus, labels, test_size=.3)

        if self.evaluate:
            corpus, X_test, labels, y_test = ms.train_test_split(corpus, labels, test_size=.3)

            