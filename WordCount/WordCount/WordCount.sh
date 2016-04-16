confLocation=WordCount.conf &&
dos2unix $confLocation &&
executors=4 &&
memory=2g &&
entry_function=count_words &&
spark-submit \
    --master spark://master:7077\
    WordCount.py $entry_function $confLocation
