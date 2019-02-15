# BQUtil

This provides a utility for exporting query plans from BigQuery.


## Usage


```py
bqutil.py <project> [k] [k1]
```

## Example Output

```json
{"id": "myproject:US.bquxjob_abc_123", "kind": "bigquery#job", "jobReference": {"projectId": "myproject", "jobId": "bquxjob_abc_123", "location": "US"}, "state": "DONE", "statistics": {"creationTime": 1550158672196.0, "startTime": 1550158672356.0, "endTime": 1550158674386.0, "totalBytesProcessed": "3536280000", "totalSlotMs": "39898", "query": {"queryPlan": [{"name": "S00: Input", "id": "0", "startMs": "1550158672576", "endMs": "1550158674215", "waitRatioAvg": 0.5344180225281602, "waitMsAvg": "427", "waitRatioMax": 0.5857321652065082, "waitMsMax": "468", "readRatioAvg": 0.43679599499374216, "readMsAvg": "349", "readRatioMax": 1.0, "readMsMax": "799", "computeRatioAvg": 0.55819774718398, "computeMsAvg": "446", "computeRatioMax": 0.9912390488110138, "computeMsMax": "792", "writeRatioAvg": 0.007509386733416771, "writeMsAvg": "6", "writeRatioMax": 0.05131414267834793, "writeMsMax": "41", "shuffleOutputBytes": "35416", "shuffleOutputBytesSpilled": "0", "recordsRead": "116280000", "recordsWritten": "1292", "parallelInputs": "92", "completedParallelInputs": "92", "status": "COMPLETE", "steps": [{"kind": "READ", "substeps": ["$2:category, $3:sales_amt, $4:qty, $1:date", "FROM mydataset.mytable", "WHERE and(greater_or_equal($1, 17318), less($1, 17410))"]}, {"kind": "AGGREGATE", "substeps": ["GROUP BY $30 := $2", "$20 := SUM($3)", "$21 := SUM($4)"]}, {"kind": "WRITE", "substeps": ["$30, $20, $21", "TO __stage00_output", "BY HASH($30)"]}]}, {"name": "S01: Output", "id": "1", "startMs": "1550158674245", "endMs": "1550158674298", "inputStages": ["0"], "waitRatioAvg": 0.0, "waitMsAvg": "0", "waitRatioMax": 0.0012515644555694619, "waitMsMax": "1", "readRatioAvg": 0.0, "readMsAvg": "0", "readRatioMax": 0.0, "readMsMax": "0", "computeRatioAvg": 0.006257822277847309, "computeMsAvg": "5", "computeRatioMax": 0.007509386733416771, "computeMsMax": "6", "writeRatioAvg": 0.007509386733416771, "writeMsAvg": "6", "writeRatioMax": 0.012515644555694618, "writeMsMax": "10", "shuffleOutputBytes": "289", "shuffleOutputBytesSpilled": "0", "recordsRead": "1292", "recordsWritten": "17", "parallelInputs": "9", "completedParallelInputs": "9", "status": "COMPLETE", "steps": [{"kind": "READ", "substeps": ["$30, $20, $21", "FROM __stage00_output"]}, {"kind": "AGGREGATE", "substeps": ["GROUP BY $40 := $30", "$10 := SUM($20)", "$11 := SUM($21)"]}, {"kind": "WRITE", "substeps": ["$10, $11", "TO __stage01_output"]}]}], "estimatedBytesProcessed": "3536280000", "timeline": [{"elapsedMs": "718", "totalSlotMs": "338", "pendingUnits": "87", "completedUnits": "5", "activeUnits": "87"}, {"elapsedMs": "1222", "totalSlotMs": "11368", "pendingUnits": "58", "completedUnits": "34", "activeUnits": "87"}, {"elapsedMs": "1999", "totalSlotMs": "55812", "pendingUnits": "0", "completedUnits": "101", "activeUnits": "6"}], "totalPartitionsProcessed": "92", "totalBytesProcessed": "3536280000", "totalBytesBilled": "3536846848", "billingTier": 1, "totalSlotMs": "39898", "cacheHit": false, "referencedTables": [{"projectId": "myproject", "datasetId": "mydataset", "tableId": "mytable"}], "statementType": "SELECT"}}, "configuration": {"jobType": "QUERY", "query": {"query": "select sum(sales_amt) sales_amt, sum(qty) qty\nfrom mydataset.mytable\nwhere date >= '2017-06-01' and date < '2017-09-01'\ngroup by category\n", "destinationTable": {"projectId": "myproject", "datasetId": "_abc123", "tableId": "anonabc123"}, "createDisposition": "CREATE_IF_NEEDED", "writeDisposition": "WRITE_TRUNCATE", "priority": "INTERACTIVE", "allowLargeResults": false, "useQueryCache": true, "useLegacySql": false}}, "status": {"state": "DONE"}, "user_email": "user@example.com"}
```

## File Layout
- [bqutil.py](bqutil/bqutil.py) BigQuery client wrapper and command-line executable


## Installation

### Optional: Install in virtualenv

```
python3 -m virtualenv venv
source venv/bin/activate
```

### Install with pip

```
python3 -m pip install git+https://github.com/jasonmar/bqutil
```

### Install with setup.py

```
pip3 install -r requirements.txt
python3 setup.py build
python3 setup.py install
```


## Requirements

You'll need to [download Python 3.4 or later](https://www.python.org/downloads/)

[Google Cloud Python Client](https://github.com/googleapis/google-cloud-python)


### pip

```
python3 -m pip install --user --upgrade pip
```

### Optional: virtualenv

```
python3 -m pip install --user virtualenv
```

## Disclaimer

This is not an official Google project.


## References

[Python Example Code](https://github.com/GoogleCloudPlatform/python-docs-samples)
[google-cloud-bigquery](https://pypi.org/project/google-cloud-bigquery/)
