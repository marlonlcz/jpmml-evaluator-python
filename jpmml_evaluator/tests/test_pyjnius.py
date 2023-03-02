from jpmml_evaluator.pyjnius import jnius_configure_classpath, PyJNIusBackend

from . import EvaluatorTest

class PyJNIusEvaluatorTest(EvaluatorTest):

	def setUp(self):
		jnius_configure_classpath()

	def tearDown(self):
		pass

	def test_pyjnius(self):
		backend = PyJNIusBackend()
		super(PyJNIusEvaluatorTest, self).workflow(backend, lax = True)
