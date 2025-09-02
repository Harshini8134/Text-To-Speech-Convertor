A deep-learning based Text-to-Speech (TTS) system that converts input text into natural-sounding audio. This repository contains code for data preprocessing, model training (neural TTS), inference, and evaluation.
Overview

This project implements a neural TTS pipeline using modern deep learning techniques (examples: Tacotron 2 for spectrogram prediction and a neural vocoder such as WaveGlow / HiFi-GAN for waveform synthesis). The repository is structured to let you train from scratch on your own dataset or run inference with pretrained checkpoints.

Key goals:

Produce intelligible, natural-sounding synthetic speech

Modular code: preprocessing, model, trainer, and inference

Reproducible training and evaluation scripts

⚙️ Features

Text normalization and phoneme/token conversion

Spectrogram generation (Mel-spectrogram) and inversion

Tacotron-style seq2seq spectrogram predictor

Neural vocoder (HiFi-GAN compatible) for waveform generation

Training, validation, and checkpointing

Simple CLI for inference
