#!/usr/bin/env python

import beanstalkc
import json
import sys

print "Getting build details from jenkins"
beanstalk_host = sys.argv[1]
image_details = {}
image_details["action"] = "start_scan"
image_details["namespace"] = sys.argv[2]
image_details["output_image"] = sys.argv[3]
image_details["test_tag"] = sys.argv[4]
image_details["notify_email"] = sys.argv[5]
image_details["logs_dir"] = sys.argv[6]
image_details["job_name"] = sys.argv[7]
image_details["image_name"] = sys.argv[8]
print "Pushing image details in the tube"
bs = beanstalkc.Connection(host=beanstalk_host)
bs.use("master_tube")
bs.put(json.dumps(image_details))
print "image details is pushed to tube for testing"
