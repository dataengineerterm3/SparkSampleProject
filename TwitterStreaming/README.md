###Twitter Streaming Geo Tracking
===========================================
**1.** run src/twitter_streaming.py : spark-submit dir/src/twitter_streaming.py
- sample results
"""
-------------------------------------------
Time: 2016-04-22 22:06:00
-------------------------------------------
{"user_id": 3261513740, "screen_name": "white2521", "timestamp": "2016-04-23T05:05:57", "hashtags": [], "text": "RT @ue_cydk: \u3084\u3081\u308d\u2026\u2026\u3084\u3081\u308d\u2026\u2026\u2026\u2026 https://t.co/AK1TblhBrg", "geo": null, "id": 723739666835361792}
......
-------------------------------------------
Time: 2016-04-22 22:06:10
-------------------------------------------
{"user_id": 2893566547, "screen_name": "kkkmnytk2", "timestamp": "2016-04-23T05:05:58", "hashtags": [], "text": "@arashi5_moeka \u3046\u3061\u306e\u9854\u3001\u308f\u304b\u308a\u307e\u3059\u304b\uff1f\u7b11\u7b11", "geo": null, "id": 723739671017082881}
......
-------------------------------------------
Time: 2016-04-22 22:06:20
-------------------------------------------
{"user_id": 696798184945926144, "screen_name": "ifimayinterject", "timestamp": "2016-04-23T05:05:58", "hashtags": [], "text": "@SNTranquillo isn't it \"Quick's\" job to stop the puck? https://t.co/7tCZg7wliK", "geo": null, "id": 723739671021281283}
......
"""

**2.** Kmean cluster of locations

