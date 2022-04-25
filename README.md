# lightning-pod
[![](https://img.shields.io/badge/PyTorch_Lightning-Code-informational?style=flat&logo=pytorchlightning&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Grid.ai-Compute-informational?style=flat&logo=grid.ai&logoColor=white&color=2bbc8a)](#)
[![](https://img.shields.io/badge/Gitpod-DevEnv-informational?style=flat&logo=gitpod&logoColor=white&color=2bbc8a)](#)


A template repo for [PyTorch Lightning](https://www.pytorchlightning.ai/) in [Gitpod](https://www.gitpod.io/).

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JustinGoheen/lightning-pod)

## The basics

This template can aid in creating and sharing reproducible projects structured according to potential best practices for Research Engineers.

The intent is that you clone the repo each time you need to begin a fresh project. The repo can be cloned from within VS Code, PyCharm, GitKraken, or in terminal with:

```sh
git clone https://github.com/JustinGoheen/lightning-pod.git --depth 1 --branch main --single-branch
```

## The environment

Installing pytorch-lightning also installs: 

- [PyTorch](https://pytorch.org/docs/stable/index.html)
- [torchmetrics](https://torchmetrics.readthedocs.io/en/stable/)
- [NumPy](https://numpy.org/)
- [TensorBoard](https://www.tensorflow.org/tensorboard)

In addition to PyTorch Lightning, requirements.txt will also install: 
- [lightning-transformers](https://lightning-transformers.readthedocs.io/en/latest/)
- [Grid.ai](https://www.grid.ai/)
- Hugging Face's [datasets](https://huggingface.co/docs/datasets/index)
- [SymPy](https://www.sympy.org/en/index.html) (symbolic mathematics)
- [Plotly](https://plotly.com/python/) (data visualization)
- [Black](https://black.readthedocs.io/en/stable/) (formatting)
- [MyPy](https://github.com/python/mypy/tree/38f1e30e8137ccc1aad6a4f113eb4360c6206539) (static type checker)
- [easy-sphinx](https://github.com/JustinGoheenOrg/easy-sphinx) (Sphinx-autodoc + [material for mkdocs](https://squidfunk.github.io/mkdocs-material/))

Security minded engineers can opt for [deepsource](https://deepsource.io/), [pyre/pysa](https://pyre-check.org/), or [Bandit](https://github.com/PyCQA/bandit). This template uses deepsource.

> remove the `.deepsource.toml` file if using pyre/pysa or bandit

The Gitpod config file installs the Jupyter extension for individuals who also prefer notebook environments.

## Suggested use

This template is mostly for distributed teams who can benefit from a tool like Gitpod. Individuals who wish to share open source work can use this template as a guideline for creating reproducible projects. Use of Gitpod is not required for individuals who do not fit into one of those two categories; these individuals will still benefit from forking the repo as a template and simply removing the `.gitpod.yml` file from the project directory. 

It is not recommended to start a Grid Session from within a Gitpod Workspace; doing so may accrue compute hours in both platforms.

The best practice would be to: develop in Gitpod using a development-sized (toy) dataset (i.e. fast_dev_run in PyTorch Lightning) and then start the Grid Session locally from your machine (i.e. all updates have been pushed to GitHub and the Gitpod Workspace has been shutdown).

Once the full project requirements have been determined, it is best to replace the current requirements.txt with

```sh
pip freeze > requirements.txt
```

## TensorBoard

VS Code users can learn more about PyTorch development and Tensorboard in VS Code here -> https://code.visualstudio.com/docs/datascience/pytorch-support.

Grid.ai support Tensorboard in the [Runs web interface](https://docs.grid.ai/features/runs/Analyzing%20Runs/metric-charts#tensorboard).