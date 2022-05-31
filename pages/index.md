---
layout: default
---

Online collection of my conda environments. Kept here for consistency across computers.

For non-vim versions add `no-vim` to the file name the just before the yaml. e.g. `jupyter.yaml -> jupyter-no-vim.yaml`

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

**micro-analysis**
`micro-base` plus Controlling microscopes with pymmcore-plus and napari-micromanager

```bash
mamba env create --force --file https://ianhi.github.io.envs/envs/micro-control.yaml
```

