#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import bigquery
from datetime import datetime, timedelta
import sys
import json


class BQUtil(object):
    def __init__(self, project=None, location='US'):
        self.project = project
        self.location = location
        self.bq = None

    def get_client(self):
        if self.bq is None:
            self.bq = bigquery.Client(project=self.project, location=self.location)
        return self.bq

    def get_jobs(self, start_days_ago, end_days_ago):
        c = self.get_client()
        dt0 = datetime.utcnow() - timedelta(start_days_ago)
        dt1 = datetime.utcnow() - timedelta(end_days_ago)
        return [job._properties for job in c.list_jobs(min_creation_time=dt0, max_creation_time=dt1) if
                hasattr(job, 'query_plan')]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("\nUsage: " + sys.argv[0] + " <project> [k] [k1]")
        print("Prints jobs between k days ago and k1 days ago")
        sys.exit(1)
    project = sys.argv[1]
    k = 3
    k1 = 0
    if len(sys.argv) >= 3:
        k = int(sys.argv[2])
    if len(sys.argv) >= 4:
        k1 = int(sys.argv[3])
    bq = BQUtil(project=project)
    for job in bq.get_jobs(start_days_ago=k, end_days_ago=k1):
        print(json.dumps(job))
