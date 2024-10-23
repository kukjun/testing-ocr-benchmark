# Deep Text Recognition Benchmark

Clover AI 의 Deep Text Recognition Benchmark를 이용해서 BrainOCR 테스트를 하기 위해 생성한 Repository


## Usage

init Project(poetry)
```bash
poetry shell
poetry install
```

<br>

> saved_modes/brainocr.pt 파일이 필요
 
brainocr은 nas에 올라가있음.


<br>
<br>

ai_hub_json to txt 
```bash
poetry run python change_ai_hub_json.py
```

<br>

txt, images to mdb
```bash
# need parameter
poetry run python create_lmdb_dataset.py --inputPath "" --gtFile "" --outputPath ""
```

<br>

train
```bash
# need parameter
poetry run python3 train.py --train_data "train_data" --valid_data "valid_data" --select_data / --batch_ratio 1 --Transformation TPS --FeatureExtraction VGG --SequenceModeling BiLSTM --Prediction CTC --saved_model saved_models/brainocr.pt --FT --workers 0 --num_fiducial 20 --imgH 64 --imgW 100 --valInterval 100 --batch_size 32 --lr 0.0001 --num_iter 200000
```

<br>
<br>

