# Judge_fMRI



DurationTimePerSubject.py 给定问题持续时间（被试反应时间）的最小阈值，该脚本用于可视化每个被试低于该阈值的情况，即汇总


# Introduction
2*3
2：接受过法律教育者 & 未接受过法律教育者
3：法律思维、逻辑思维和道德思维

共48名被试，23名接受过法律教育，25名未接受法律教育者


# Data Preprocessing and Analysis
使用FMRIPrep自动化预处理数据
```
$ fmriprep-docker bids_path bids_output participant --participant_label subs --write-graph --fs-license-file license.txt
```
可见Processing.py



