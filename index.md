---
layout: default
---

Online collection of my conda environments. Kept here for consistency across computers.

**Without vim**

By default the enviroments will have `jupyterlab-vim` and `jupyterlab-vimrc` installed. To not install these add `no-vim`
to the file name the just before the yaml. e.g. `jupyter.yaml -> jupyter-no-vim.yaml`


**Choose your own environment name**

The environments come with default names, however you can use the `--name` flag to override that and use your own name.
e.g. `mamba env create --force [...] --name <YOUR ENV NAME>`


## General Usage

**jupyter**

Good setup for generic analysis. Contains numpy matplotlib etc and jupyterlab with interactive matplotlib, a nice dark theme
and vim extensions.

```bash
mamba env create --force --file https://ianhi.github.io/envs/envs/jupyter.yaml
```


## Microscopy
Everything here is based on `jupyter` and also contains `xarray`

**micro-base**

base env + napari + xarray + image loading

```bash
mamba env create --force --file https://ianhi.github.io/envs/envs/micro-base.yaml
```

**micro-analysis**

`micro-base` + scikit image and learn

```bash
mamba env create --force --file https://ianhi.github.io/envs/envs/micro-analysis.yaml
```

**micro-control**

`micro-base` plus Controlling microscopes with pymmcore-plus and napari-micromanager

```bash
mamba env create --force --file https://ianhi.github.io/envs/envs/micro-control.yaml
```

