# Antennal Lobe Simulator (als_v2)

## はじめに
本リポジトリは github.com:heewonpark/als_v2 からフォークされたものであり，github.com:KosukeArase の卒業研究に使用されたものである．

## 動作環境
### スーパーコンピュータ
- neuron_kplus (git@github.com:sc4brain/neuron_kplus.git)
    * ALS を動かす場合は nrn-7.3

### ローカルマシン，クラスタ
- neuron_kplus (git@github.com:sc4brain/neuron_kplus.git)
- Python2.7
    - NumPy
    - Matplotlib

## 実行方法
### ローカルマシン
```shell
./als_v2/src$ sh run.sh
```

### クラスタ
```shell
./als_v2/job$ qsub run.sh
```

### スーパーコンピュータ

### Result

### プログラムの構成
- analyze: 解析用 Python プログラム群
- input: 種々の入力データです．
    * estimation_data: パラメータ推定用データ，後藤さんの引き継ぎ資料参照．
    * network_info: 神経回路中の全細胞の情報 (携帯とシナプス結合) について記載したファイルがあります．
    * spiketiming: 各受容細胞の刺激に対する応答を記載しています．
        + MRN: 機械感覚需要細胞の応答
        + ORN: 性フェロモン需要細胞の応答

    * swc: 
    * synapse_info: 
    * synapse_list: 
- mod
- single-src
- takeover
- cluster_job
- fxjob
- job
- result
- src
- visualize
- estimation, single-src, takeover, fxjob: 本研究では使用していません，詳細は heewonpark の引き継ぎ資料等を参照
