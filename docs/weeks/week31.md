---
layout: default
---
# Week 31: Results, Fixed circuit

## Results table (cropped image)

|                                                      Driving results (regression networks)                                                                                              ||||||||||||||
|                           |        Manual        ||    Pilotnet v + w    ||  TinyPilotnet v + w  ||        Stacked v+w   ||  Stacked (diff) v+w  || LSTM-Tinypilotnet v + w ||DeepestLSTM-Tinypilot.||
|      Circuits             | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   |  Percentage   |   Time   | Percentage |   Time   |
|  Simple (clockwise)       |    100%    | 1min 35s |     100%   | 1min 37s |     100%   | 1min 41s |     100%   | 1min 41s |     100%   | 1min 39s |      100%     | 1min 40s |    100%    | 1min 37s | 
|Simple (anti-clockwise)    |    100%    | 1min 32s |     100%   | 1min 38s |     100%   | 1min 41s |     10%    |          |     100%   | 1min 38s |      100%     | 1min 38s |    100%    | 1min 38s |
|  Monaco (clockwise)       |    100%    | 1min 15s |     100%   | 1min 20s |     100%   | 1min 19s |     85%    |          |     45%    |          |       50%     |          |     55%    |          |
|Monaco (anti-clockwise)    |    100%    | 1min 15s |     100%   | 1min 19s |     100%   | 1min 18s |     15%    |          |     5%     |          |       35%     |          |     55%    |          |
| Nurburgrin (clockwise)    |    100%    | 1min 02s |     100%   | 1min 04s |     100%   | 1min 04s |      8%    |          |     8%     |          |       40%     |          |    100%    | 1min 04s |
|Nurburgrin (anti-clockwise)|    100%    | 1min 02s |     100%   | 1min 06s |     100%   | 1min 05s |     80%    |          |     50%    |          |       50%     |          |     80%    |          |
| CurveGP (clockwise)       |    100%    | 2min 13s |     100%   | 2min 16s |      25%   |          |      25%   |          |     25%    |          |      100%     | 2min 17s |    100%    | 2min 18s | 
| CurveGP  (anti-clockwise) |    100%    | 2min 09s |     100%   | 2min 12s |      75%   |          |      75%   |          |     75%    |          |      100%     | 2min 04s |    100%    | 2min 12s |
| Small (clockwise)         |    100%    | 1min 00s |     100%   | 1min 04s |     100%   |    59s   |      30%   |          |     100%   | 1min 06s |      100%     | 1min 07s |    100%    | 1min 05s | 
| Small (anti-clockwise)    |    100%    |    59s   |     100%   | 1min 05s |     100%   | 1min 00s |      10%   |          |     100%   | 1min 05s |      100%     | 1min 03s |    100%    | 1min 08s |


|                                                      Driving results (classification networks)                     ||||||||
|                           |        Manual        ||      5v+7w biased    ||    5v+7w balanced    ||   5v+7w imbalanced   || 
|      Circuits             | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   |
|  Simple (clockwise)       |    100%    | 1min 35s |    100%    | 1min 41s |     75%    |          |    100%    | 1min 42s |
|Simple (anti-clockwise)    |    100%    | 1min 32s |    100%    | 1min 39s |    100%    | 1min 39s |    100%    | 1min 43s |
|  Monaco (clockwise)       |    100%    | 1min 15s |    100%    | 1min 20s |     70%    |          |     85%    |          |
|Monaco (anti-clockwise)    |    100%    | 1min 15s |    100%    | 1min 18s |      8%    |          |    100%    | 1min 20s |
| Nurburgrin (clockwise)    |    100%    | 1min 02s |    100%    | 1min 03s |    100%    | 1min 03s |    100%    | 1min 05s |
|Nurburgrin (anti-clockwise)|    100%    | 1min 02s |    100%    | 1min 05s |     80%    |          |     80%    |          |
|   CurveGP (clockwise)     |    100%    | 2min 13s |    100%    | 2min 06s |     97%    |          |    100%    | 2min 15s |
| CurveGP (anti-clockwise)  |    100%    | 2min 09s |    100%    | 2min 11s |    100%    | 2min 05s |    100%    | 2min 15s |
|   Small (clockwise)       |    100%    | 1min 00s |    100%    | 1min 02s |    100%    | 1min 02s |    100%    | 1min 01s |
| Small (anti-clockwise)    |    100%    |    59s   |    100%    | 1min 03s |    100%    | 1min 03s |    100%    | 1min 04s |




## Results table (whole image)

|                                                      Driving results (regression networks)                                               ||||||||||
|                           |        Manual        ||    Pilotnet v + w    ||  TinyPilotnet v + w  ||        Stacked v+w   ||  Stacked (diff) v+w  ||
|      Circuits             | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   |
|  Simple (clockwise)       |    100%    | 1min 35s |     100%   | 1min 41s |     100%   | 1min 39s |     100%   | 1min 40s |     100%   | 1min 43s |
|Simple (anti-clockwise)    |    100%    | 1min 32s |     100%   | 1min 39s |     100%   | 1min 38s |     100%   | 1min 46s |     10%    |          |
|  Monaco (clockwise)       |    100%    | 1min 15s |     100%   | 1min 21s |     100%   | 1min 19s |     50%    |          |     5%     |          |
|Monaco (anti-clockwise)    |    100%    | 1min 15s |     100%   | 1min 23s |     100%   | 1min 20s |      7%    |          |     5%     |          |
| Nurburgrin (clockwise)    |    100%    | 1min 02s |     100%   | 1min 03s |     100%   | 1min 05s |     50%    |          |     8%     |          |
|Nurburgrin (anti-clockwise)|    100%    | 1min 02s |     100%   | 1min 06s |     100%   | 1min 06s |     80%    |          |     50%    |          |
|   CurveGP (clockwise)     |    100%    | 2min 13s |     100%   | 2min 20s |     100%   | 2min 11s |     25%    |          |     25%    |          |
| CurveGP (anti-clockwise)  |    100%    | 2min 09s |     100%   | 2min 16s |     100%   | 2min 06s |     100%   | 2min 07s |     75%    |          |
|   Small (clockwise)       |    100%    | 1min 00s |     100%   | 1min 07s |     100%   | 1min 02s |     100%   | 1min 11s |     100%   | 1min 03s |
| Small (anti-clockwise)    |    100%    |    59s   |     100%   | 1min 09s |     100%   | 1min 02s |     100%   | 1min 08s |     100%   | 1min 02s |


|                     Driving results (regression networks, continuation)                         ||||||
|                           | LSTM-Tinypilotnet v + w ||DeepestLSTM-Tinypilot.||      Controlnet      || 
|      Circuits             |  Percentage   |   Time   | Percentage |   Time   | Percentage |   Time   |
|  Simple (clockwise)       |      100%     | 1min 39s |    100%    | 1min 39s |    100%    | 1min 46s |
|Simple (anti-clockwise)    |      100%     | 1min 40s |    100%    | 1min 41s |    100%    | 1min 37s |
|  Monaco (clockwise)       |       50%     |          |     50%    |          |      5%    |          | 
|Monaco (anti-clockwise)    |       12%     |          |    100%    | 1min 21s |      5%    |          |
| Nurburgrin (clockwise)    |       20%     |          |    100%    | 1min 05s |      8%    |          |
|Nurburgrin (anti-clockwise)|       80%     |          |    100%    | 1min 07s |     75%    |          |
|   CurveGP (clockwise)     |      100%     | 2min 20s |     25%    |          |     25%    |          |
| CurveGP (anti-clockwise)  |      100%     | 2min 25s |    100%    | 2min 04s |      3%    |          |
|   Small (clockwise)       |      100%     | 1min 11s |    100%    | 1min 05s |    100%    | 1min 01s |
| Small (anti-clockwise)    |      100%     | 1min 09s |    100%    | 1min 07s |    100%    | 1min 01s |



|                                                      Driving results (classification networks)                     ||||||||
|                           |        Manual        ||      5v+7w biased    ||     5v+7w balanced   ||   5v+7w imbalanced   || 
|      Circuits             | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   | Percentage |   Time   |
|  Simple (clockwise)       |    100%    | 1min 35s |     35%    |          |     10%    |          |     90%    |          |
|Simple (anti-clockwise)    |    100%    | 1min 32s |    100%    | 1min 49s |    100%    | 1min 46s |     90%    |          |
|  Monaco (clockwise)       |    100%    | 1min 15s |    100%    | 1min 24s |      5%    |          |    100%    | 1min 23s |
|Monaco (anti-clockwise)    |    100%    | 1min 15s |    100%    | 1min 29s |      8%    |          |    100%    | 1min 24s |
| Nurburgrin (clockwise)    |    100%    | 1min 02s |    100%    | 1min 10s |      8%    |          |     90%    |          |
|Nurburgrin (anti-clockwise)|    100%    | 1min 02s |    100%    | 1min 07s |      8%    |          |    100%    | 1min 09s |
|   CurveGP (clockwise)     |    100%    | 2min 13s |    95%     |          |     80%    |          |     25%    |          |
| CurveGP (anti-clockwise)  |    100%    | 2min 09s |     7%     |          |      3%    |          |     20%    |          |
|   Small (clockwise)       |    100%    | 1min 00s |     8%     |          |      8%    |          |    100%    | 1min 08s |
| Small (anti-clockwise)    |    100%    |    59s   |     12%    |          |     12%    |          |    100%    | 1min 08s |



## Fixed circuit

* Small circuit:

![small_fixed](https://roboticslaburjc.github.io/2017-tfm-vanessa-fernandez/images/small_fixed.png)


