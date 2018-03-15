# fork of previous ones forked from Apache MXNet examples
# https://github.com/tspannhw/mxnet_rpi/blob/master/analyze.py
import time
import sys
import datetime
import subprocess
import sys
import os
import datetime
import traceback
import math
import random, string
import base64
import json
from time import gmtime, strftime
import mxnet as mx
import inception_predict
import numpy as np
import cv2
import math
import random, string
import time

from time import gmtime, strftime
start = time.time()
cap = cv2.VideoCapture(1)

packet_size=3000


# Create unique image name
uniqueid = 'mxnet_uuid_{0}_{1}'.format('img',strftime("%Y%m%d%H%M%S",gmtime()))

ret, frame = cap.read()

filename = 'images/tx1_image_{0}_{1}.jpg'.format('img',strftime("%Y%m%d%H%M%S",gmtime()))
cv2.imwrite(filename, frame)

topn = []
# Run inception prediction on image
try:
     topn = inception_predict.predict_from_local_file(filename, N=5)
except:
     print("Error")
     errorcondition = "true"

try:
     # 5 MXNET Analysis
     top1 = str(topn[0][1])
     top1pct = str(round(topn[0][0],3) * 100)

     top2 = str(topn[1][1])
     top2pct = str(round(topn[1][0],3) * 100)

     top3 = str(topn[2][1])
     top3pct = str(round(topn[2][0],3) * 100)

     top4 = str(topn[3][1])
     top4pct = str(round(topn[3][0],3) * 100)

     top5 = str(topn[4][1])
     top5pct = str(round(topn[4][0],3) * 100)

     end = time.time()

     row = { 'uuid': uniqueid,  'top1pct': top1pct, 'top1': top1, 'top2pct': top2pct, 'top2': top2,'top3pct': top3pct, 'top3': top3,'top4pct': top4pct,'top4': top4, 'top5pct': top5pct,'top5': top5, 'imagefilename': filename, 'runtime': str(round(end - start)) }
     json_string = json.dumps(row)

     print (json_string )
except:
     print("{\"message\": \"Failed to run\"}")
