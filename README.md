# Can VLMs Hear What They See?

An experimental exploration of using Vision Language Models (VLMs) for audio classification through spectrogram analysis.

## Overview

This project explores whether VLMs can effectively classify audio by analyzing spectrograms, inspired by the paper [Vision Language Models Are Few-Shot Audio Spectrogram Classifiers](https://arxiv.org/abs/2411.12058). Using the ESC-10 environmental sound dataset, we:

- Generate and analyze spectrograms from audio samples
- Compare embeddings from different models (CLAP, Music2Latent, AIMv2)
- Implement zero-shot classification using Janus-Pro VLM
- Evaluate performance against CLAP as a baseline

## Key Findings

- Audio-specific models (CLAP) show superior performance in zero-shot classification

- Visual embedding analysis reveals challenges in treating audio classification as a pure visual task

- VLMs show potential but require more sophisticated approaches (few-shot learning, better prompting) for competitive performance

## Requirements

- Python 3.11+
- FiftyOne
- PyTorch
- Transformers
- Additional requirements in `requirements.txt`

## Getting Started

1. Clone this repository

2. Install dependencies: `pip install -r requirements.txt`

3. Follow the Jupyter notebook `main_noteblog.ipynb` for the complete analysis

## Data

The project uses the ESC-10 dataset, a curated subset of ESC-50 containing 400 environmental sound recordings across 10 classes.

## Tools Used

- FiftyOne for dataset management and visualization
- CLAP for audio embeddings and classification
- Music2Latent for audio feature extraction
- AIMv2 for visual embeddings
- Janus-Pro for zero-shot visual classification


## Acknowledgments

- Original paper authors for the inspiration
- ESC-10 dataset creators
- FiftyOne team for the visualization tools

# Citations

#### Vision Language Models are Few-Shot Audio Spectrogram Classifiers

```bibtex
@article{dixit2024vision,
    title={Vision Language Models Are Few-Shot Audio Spectrogram Classifiers},
    author={Dixit, Satvik and Heller, Laurie M. and Donahue, Chris},
    journal={arXiv preprint arXiv:2411.12058},
    year={2024},
    archivePrefix={arXiv},
    eprint={2411.12058},
    primaryClass={cs.SD}
}
```

#### ESC Dataset

```bibtex
@inproceedings{piczak2015dataset,
  title = {{ESC}: {Dataset} for {Environmental Sound Classification}},
  author = {Piczak, Karol J.},
  booktitle = {Proceedings of the 23rd {Annual ACM Conference} on {Multimedia}},
  date = {2015-10-13},
  url = {http://dl.acm.org/citation.cfm?doid=2733373.2806390},
  doi = {10.1145/2733373.2806390},
  location = {{Brisbane, Australia}},
  isbn = {978-1-4503-3459-4},
  publisher = {{ACM Press}},
  pages = {1015--1018}
}
```

#### Music2Latent

```bibtex
@inproceedings{pasini2024music2latent,
    title={Music2Latent: Consistency Autoencoders for Latent Audio Compression},
    author={Pasini, Marco and Lattner, Stefan and Fazekas, George},
    booktitle={Proceedings of the International Society for Music Information Retrieval Conference (ISMIR)},
    year={2024},
    archivePrefix={arXiv},
    eprint={2408.06500},
    primaryClass={cs.SD}
}
```
### AIMv2

```bibtex
@misc{fini2024multimodal,
    title={Multimodal Autoregressive Pre-training of Large Vision Encoders},
    author={Enrico Fini and Mustafa Shukor and Xiujun Li and Philipp Dufter and Michal Klein and David Haldimann and Sai Aitharaju and Victor Guilherme Turrisi da Costa and Louis Béthune and Zhe Gan and Alexander T Toshev and Marcin Eichner and Moin Nabi and Yinfei Yang and Joshua M. Susskind and Alaaeldin El-Nouby},
    year={2024},
    eprint={2411.14402},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

#### CLAP

```bibtex
@misc{https://doi.org/10.48550/arxiv.2211.06687,
  doi = {10.48550/ARXIV.2211.06687},
  url = {https://arxiv.org/abs/2211.06687},
  author = {Wu, Yusong and Chen, Ke and Zhang, Tianyu and Hui, Yuchen and Berg-Kirkpatrick, Taylor and Dubnov, Shlomo},
  keywords = {Sound (cs.SD), Audio and Speech Processing (eess.AS), FOS: Computer and information sciences, FOS: Computer and information sciences, FOS: Electrical engineering, electronic engineering, information engineering, FOS: Electrical engineering, electronic engineering, information engineering},
  title = {Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```
#### Janus-Pro

```bibtex
@misc{chen2025januspro,
      title={Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling}, 
      author={Xiaokang Chen and Zhiyu Wu and Xingchao Liu and Zizheng Pan and Wen Liu and Zhenda Xie and Xingkai Yu and Chong Ruan},
      year={2025},
}
```