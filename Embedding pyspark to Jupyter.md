- _reference_
  -  https://www.dataquest.io/blog/installing-pyspark/  
  -  http://npatta01.github.io/2015/08/01/pyspark_jupyter/
- _steps_
  - test with pyspark : run $SPARK_HOME$/bin/pyspark
  - Environment variables :
    - export SPARK_HOME="$HOME/spark-1.6xx"
    - export PYSPARK_SUBMIT_ARGS="--master local[2]"
    - export PATH=$SPARK_HOME/bin:$PATH
    - export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
    - export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.xx(check your version)-src.zip:$PYTHONPATH
  - IPython profile
    -  run "ipython profile create pyspark"
    -  create "~/.ipython/profile_pyspark/startup/00-pyspark-setup.py" with vim/nano, copy the following code, change the versions of spark and py4j.

```python
import os
import sys

spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, spark_home + "/python")
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.XXX-src.zip'))

filename = os.path.join(spark_home, 'python/pyspark/shell.py')
exec(compile(open(filename, "rb").read(), filename, 'exec'))

spark_release_file = spark_home + "/RELEASE"

if os.path.exists(spark_release_file) and "Spark 1.X" in open(spark_release_file).read():
    pyspark_submit_args = os.environ.get("PYSPARK_SUBMIT_ARGS", "")
    if not "pyspark-shell" in pyspark_submit_args: 
        pyspark_submit_args += " pyspark-shell"
        os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args
```
   - run "ipython notebook --profile=pyspark"



