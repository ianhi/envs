---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

Online collection of my conda environments. Kept here for consistency across computers.

For non-vim versions use the `envs/no_vim` folder and add `no-vim` to the file name.


## Microscopy

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

