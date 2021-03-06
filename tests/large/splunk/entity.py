import json


def getEntities(endpoint, count, sessionKey):
    return json.loads(
        """
{
  "film.json": {
    "mode": "sample",
    "end": "1",
    "eai:userName": "admin",
    "source": "film.json",
    "eai:acl": {
      "removable": "0",
      "can_share_global": "1",
      "perms": {
        "read": [
          "*"
        ],
        "write": [
          "*"
        ]
      },
      "can_list": "1",
      "can_share_app": "1",
      "app": "modinput_test_app",
      "sharing": "global",
      "can_share_user": "0",
      "can_write": "1",
      "owner": "nobody",
      "can_change_perms": "1",
      "modifiable": "1"
    },
    "sampletype": "raw",
    "eai:appName": "search",
    "sourcetype": "json",
    "count": "10",
    "disabled": "0",
    "index": "main"
  },
  "global": {
    "generator": "default",
    "delay": "0",
    "splunkMethod": "https",
    "eai:userName": "admin",
    "maxQueueLength": "0",
    "mode": "sample",
    "eai:acl": {
      "removable": "0",
      "can_share_global": "1",
      "perms": {
        "read": [
          "*"
        ],
        "write": [
          "admin"
        ]
      },
      "can_list": "1",
      "can_share_app": "1",
      "app": "SA-Eventgen",
      "sharing": "global",
      "can_share_user": "0",
      "can_write": "1",
      "owner": "nobody",
      "can_change_perms": "1",
      "modifiable": "1"
    },
    "rater": "config",
    "interval": "60",
    "disabled": "0",
    "useOutputQueue": "0",
    "autotimestamp": "0",
    "threading": "thread",
    "eai:appName": "search",
    "sourcetype": "eventgen",
    "count": "-1",
    "outputWorkers": "1",
    "timeField": "_raw",
    "source": "eventgen",
    "sampletype": "raw",
    "timeMultiple": "1",
    "outputMode": "modinput",
    "httpeventWaitResponse": "1",
    "splunkPort": "8089",
    "verbose": "0",
    "host": "127.0.0.1",
    "profiler": "0",
    "generatorWorkers": "1",
    "fileMaxBytes": "10485760",
    "index": "main",
    "maxIntervalsBeforeFlush": "3",
    "debug": "0",
    "spoolFile": "<SAMPLE>",
    "earliest": "now",
    "randomizeEvents": "0",
    "fileBackupFiles": "5",
    "breaker": "\\n",
    "spoolDir": "$SPLUNK_HOME/var/spool/splunk",
    "latest": "now"
  }
}
"""
    )
