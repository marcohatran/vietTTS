from argparse import Namespace
from pathlib import Path
from typing import NamedTuple

from jax.numpy import ndarray


class FLAGS(Namespace):
  duration_lstm_dim = 256
  vocab_size = 256
  duration_embed_dropout_rate = 0.5
  num_training_steps = 100_000
  postnet_dim = 512
  acoustic_decoder_dim = 512
  acoustic_encoder_dim = 256

  # dataset
  max_phoneme_seq_len = 128 * 3
  max_wave_len = 1024 * 64 * 3

  # dsp
  mel_dim = 80
  n_fft = 1024
  sample_rate = 16000
  fmin = 0.0
  fmax = 8000

  # training
  batch_size = 64
  learning_rate = 3e-4
  max_grad_norm = 1.0

  # ckpt
  ckpt_dir = Path('assets/infore/nat')
  data_dir = Path('assets/infore/data')
  data_dir = Path('train_data')


class DurationInput(NamedTuple):
  phonemes: ndarray
  lengths: ndarray
  durations: ndarray


class AcousticInput(NamedTuple):
  phonemes: ndarray
  lengths: ndarray
  durations: ndarray
  wavs: ndarray
  wav_lengths: ndarray
  mels: ndarray
