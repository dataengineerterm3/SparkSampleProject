
import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from flask import Flask, render_template, Response
import redis
import json

app = Flask(__name__)
r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

def event_stream():
    pubsub = r.pubsub()
    pubsub.subscribe('data')
    for m in pubsub.listen():
        print m
        print 'Recieved: {0}'.format(m['data'])

def takeAndPrint(time, rdd, num=1000):
    result = []
    taken = rdd.take(num + 1)
    print("-------------------------------------------")
    print("Time: %s" % time)
    print("-------------------------------------------")
    for record in taken[:num]:
        print(record)
        result.append(record)

    if len(taken) > num:
        print("...")
    print("")

if __name__ == "__main__":
    

	# Create a local StreamingContext with working thread and batch interval of 1 second        
    sc = SparkContext(event_stream())
    ssc = StreamingContext(sc, 1)

    lines = ssc.socketTextStream('127.0.0.1', int(6379))
    counts = lines.flatMap(lambda line: line.split(" "))
    # Pretty print
    print counts
    counts.foreachRDD(takeAndPrint)
    # Start the computation
    ssc.start()


    # Wait for the computation to terminate
    ssc.awaitTermination()