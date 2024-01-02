# Judge_fMRI
This repo is for data analysis of a historical data.

# Introduction

## Experimental design
A 2 (between-subject: legal pro vs. non-legal pro) by 3 (Question type: logical, moral, or legal) mixed design. 

共48名被试，23名接受过法律教育，25名未接受法律教育者


# Data Preprocessing and Analysis
## Behavioral data
DurationTimePerSubject.py 给定问题持续时间（被试反应时间）的最小阈值，该脚本用于可视化每个被试低于该阈值的情况，即汇总

## fMRI data preprocessing
使用[FMRIPrep vXXX](fmriprep.readthedocs.io/)自动化预处理数据

```
$ fmriprep-docker bids_path bids_output participant --participant_label subs --write-graph --fs-license-file license.txt
```

可见`Processing.py`



