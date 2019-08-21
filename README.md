SCUT-FBP5500 - FastAI Dataset
=================================

This is a processed version of original [SCUT-FBP5500](https://github.com/HCIILAB/SCUT-FBP5500-Database-Release).

## 1. Description

The SCUT-FBP5500 dataset has totally 5500 frontal faces with diverse properties
(male/female, Asian/Caucasian, ages) and diverse labels (facial landmarks, beauty scores in 5 scales, beauty score distribution), which allows different computational model with different facial beauty prediction paradigms, such as appearance-based/shape-based facial beauty classification/regression/ranking model for male/female of Asian/Caucasian.

## 2. Citation

Please, cite their work. This dataset should only be used for non-commercial research purposes.

```
@article{liang2017SCUT,
  title     = {SCUT-FBP5500: A Diverse Benchmark Dataset for Multi-Paradigm Facial Beauty Prediction},
  author    = {Liang, Lingyu and Lin, Luojun and Jin, Lianwen and Xie, Duorui and Li, Mengru},
  jurnal    = {ICPR},
  year      = {2018}
}
```

## Desclaimer

I'm not the creator nor mantainer of the original dataset. Just made the script `convert_to_fastai_csv.py` which converts the dataset for a easier way to use on FastAI Library.
