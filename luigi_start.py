import luigi

class MyExampleTask(luigi.Task):

    report_date = luigi.DateParameter()

    def requires(self):
        """
        Which other Tasks need to be complete before this Task can start?
        Essentially returns a list of the dependencies, which are also the inputs.
        """
        return [MyUpstreamTask(self.report_date)]
        # Here the upstream task is the class MyUpstreamTask, which takes 
        # the report date from this class as it's input. Thus the task is run and the output is returned

    def output(self):
        pass

    def run(self):
        pass