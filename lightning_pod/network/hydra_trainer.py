"""
This module serves to consolidate basic use cases of PyTorch Lightning and to test
functionality of this template using an encoder-decoder on MNIST. Documentation and soruce
code links are provided below.

example code: https://pytorch-lightning.readthedocs.io/en/latest/model/train_model_basic.html
Trainer: https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html
Trainer source code: https://github.com/PyTorchLightning/pytorch-lightning/blob/eb21135b2aad20aaad45aae44858c090f1e780e5/pytorch_lightning/trainer/trainer.py#L126
Reproducibility: https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html#reproducibility
TensorBoardLogger: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.loggers.tensorboard.html#tensorboard
SimpleProfiler: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.profiler.SimpleProfiler.html#simpleprofiler
ModelCheckpoint: https://pytorch-lightning.readthedocs.io/en/latest/api/pytorch_lightning.callbacks.ModelCheckpoint.html#modelcheckpoint
"""

import os
import hydra
from pathlib import Path
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning.profiler import SimpleProfiler
from pytorch_lightning.callbacks import ModelCheckpoint, EarlyStopping
from lightning_pod.network.module import LitModel
from lightning_pod.pipeline.datamodule import LitDataModule

NETWORKPATH = Path(__file__).parent
PODPATH = NETWORKPATH.parents[0]
PROJECTPATH = NETWORKPATH.parents[1]
CFGPATH = os.path.join(NETWORKPATH, "config.yml")


@hydra.main(config_path=NETWORKPATH, config_name="config.yaml")
def main(cfg):
    # GET CURRENT WORKING DIRECTORY
    # SET LOGGER
    logs_dir = os.path.join(PROJECTPATH, "logs")
    logger = TensorBoardLogger(logs_dir, name="lightning_logs")
    # SET PROFILER
    profile_dir = os.path.join(logs_dir, "profiler")
    profiler = SimpleProfiler(dirpath=profile_dir, filename="profiler", extended=True)
    # SET CHECKPOINT CALLBACK
    chkpt_dir = os.path.join(PROJECTPATH, "models", "checkpoints")
    checkpoint_callback = ModelCheckpoint(dirpath=chkpt_dir, filename="model")
    # SET EARLYSTOPPING CALLBACK
    early_stopping = EarlyStopping(monitor="loss", mode="min")
    # SET CALLBACKS
    callbacks = [checkpoint_callback, early_stopping]
    # SET SEED
    seed_everything(42, workers=True)
    #  GET DATALOADER
    datamodule = LitDataModule()
    #  SET MODEL
    model = LitModel()
    # SET TRAINER
    trainer = Trainer(
        max_epochs=cfg.training.max_epochs,
        limit_train_batches=cfg.training.limit_train_batches,  # use only x% of training samples
        limit_predict_batches=None,
        limit_test_batches=None,
        limit_val_batches=None,
        accelerator=cfg.training.accelerator,
        devices=cfg.training.devices,
        deterministic=cfg.training.deterministic,  # for reproducibility
        strategy=cfg.training.strategy,
        precision=cfg.training.precision,
        enable_model_summary=cfg.training.enable_model_summary,
        enable_checkpointing=cfg.training.enable_checkpointing,
        enable_progress_bar=cfg.training.enable_progress_bar,
        logger=logger,
        profiler=profiler,
        callbacks=callbacks,
        plugins=None,  # defaults flags
        default_root_dir=None,
        gradient_clip_val=None,
        gradient_clip_algorithm=None,
        num_nodes=1,
        num_processes=None,
        gpus=None,
        auto_select_gpus=False,
        tpu_cores=None,
        ipus=None,
        overfit_batches=0.0,
        track_grad_norm=-1,
        check_val_every_n_epoch=1,
        fast_dev_run=False,
        accumulate_grad_batches=None,
        min_epochs=None,
        max_steps=-1,
        min_steps=None,
        max_time=None,
        val_check_interval=None,
        flush_logs_every_n_steps=None,
        log_every_n_steps=50,
        sync_batchnorm=False,
        weights_save_path=None,
        weights_summary="top",
        num_sanity_val_steps=2,
        resume_from_checkpoint=None,
        benchmark=None,
        reload_dataloaders_every_n_epochs=0,
        auto_lr_find=False,
        replace_sampler_ddp=True,
        detect_anomaly=False,
        auto_scale_batch_size=False,
        amp_backend="negative",  # amp is "automatic mixed precision"
        amp_level=None,
        move_metrics_to_cpu=False,
        multiple_trainloader_mode="max_size_cycle",
    )
    # TRAIN MODEL https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#fit
    trainer.fit(model=model, datamodule=datamodule)
    # TEST MODEL
    trainer.test(datamodule=datamodule)
    # PERSIST MODEL
    pretrained_dir = os.path.join(PROJECTPATH, "models", "production")
    modelpath = os.path.join(pretrained_dir, "model.onnx")
    input_sample = datamodule.train_data.dataset[0][0]
    model.to_onnx(modelpath, input_sample=input_sample, export_params=True)


if __name__ == "__main__":
    main()