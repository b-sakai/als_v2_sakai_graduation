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
./als_v2/cluster_job$ qsub job.sh
```

### スーパーコンピュータ (京)
```shell
./als_v2/job$ pjsub run_with_mechano.sh
```

### Result
`.sh` ファイル内で指定しているディレクトリ内に Job ID と同名のディレクトリが作られ，その中にシミュレーション結果が保存される
- out: 標準出力
- record: 単位時間毎の膜電位
- spike: スパイクが立ったタイミング，cluster で実行する場合，LN, PN については draw_PSTH.py によってグラフも作成される

### プログラムの構成
__プログラムの詳細については `./takeover/hikitsugi_park_ver20160613.pdf` を参照__

- analyze: 解析用 Python プログラム群
- input: 種々の入力データ
    * estimation_data: パラメータ推定用データ，後藤さんの引き継ぎ資料参照
    * network_info: 神経回路中の全細胞の情報 (携帯とシナプス結合) について記載したファイル
    * spiketiming: 各受容細胞の刺激に対する応答を記載．
        + MRN: 機械感覚需要細胞の応答
        + ORN: 性フェロモン需要細胞の応答
    * swc: ニューロンの形状を記載した SWC ファイル，`xxx_mkRegion.swc` を利用
    * synapse_info: 各ニューロンのペアについて，結合しているコンパートメントとその id についての情報
    * synapse_list: ニューロンの結合情報，synapse_info への参照をもつ
- src: マルチコンパートメントシミュレーション用のソースコード
- single-src: シングルコンパートメントシミュレーション用のソースコード
- cluster_job: ラボのクラスタにジョブを投げる際に利用する `.sh`
- job: 京にジョブを投げる際に利用する `.sh`
- mod: nmodl ファイル- mod: nmodl ファイル
- takeover: 朴さんによる引き継ぎ資料
- visualize: ParaView により可視化する際に用いる vtk ファイルを作成
- estimation, fxjob: 本研究では使用していません

### パラメータ
job ファイル内の `NRNOPT` で指定
- STOPTIME: シミュレーション時間
- IS_SUPERCOMPUTER: ローカルは 0，京は 1，cluster は 2 を指定
- INTERVAL: 連続刺激を行う場合の刺激間インターバル
- SAVE_ALL: 描画用に全てのニューロンの電位を保存する場合は 1 を指定
- NCELL: 細胞数
- WEIGHT_200: 性フェロモン受容細胞から PN への結合強度
- WEIGHT_300: 性フェロモン受容細胞から 300 系 LN への結合強度
- WEIGHT_301: 性フェロモン受容細胞から 301 系 LN への結合強度
- WEIGHT_M: 機械感覚受容細胞から各細胞への結合強度
- WEIGHT_GO_300: 一般臭 (General Odor) 受容細胞から 300 系 LN への結合強度
- WEIGHT_GO_301: 一般臭 (General Odor) 受容細胞から 301 系 LN への結合強度
- COMP_X: 膜電位を保存する LN コンパートメント (SAVE_ALL=1 の場合は不要)
- GABAA_ON: GABA A を有効にするかどうか
- GABAB_ON: GABA B を有効にするかどうか
- DOSE: 性フェロモン濃度
- NSTIM: 刺激回数
- MECHANO_SPONTANEOUS: 機械感覚受容細胞の自然発火周波数
- MECHANO_ON: 機械感覚受容細胞からの入力を有効にするかどうか
- GENERAL_ODOR_ON: 一般臭受容細胞からの入力を有効にするかどうか
- GABAA_GMAX_LTOP: LN → PN の GABA A の最大コンダクタンス
- GABAA_GMAX_LTOL: LN → LN の GABA A の最大コンダクタンス
- GABAB_GMAX_LTOP: LN → PN の GABA B の最大コンダクタンス
- GABAB_GMAX_LTOL: LN → LN の GABA B の最大コンダクタンス
- GBAR_TIMES_LN: LN における細胞内伝達に関するパラメータにかける定数 (伝達しやすさを調整)
- GBAR_TIMES_PN: PN における細胞内伝達に関するパラメータにかける定数 (伝達しやすさを調整)


### 各データ他の保存場所
卒業論文: `synapse:/home/common/ResearchProducts/卒業研究/平成28年度/Arase`
ソースコード: https://github.com/KosukeArase/als_v2
京上での実行スクリプトと結果: `K:/home/hp160269/k03367/als_v2`
クラスタ上での実行スクリプトと結果: `cluster:/home/arase/kanzaki_lab/als_v2`
# als_v2_sakai_graduation
