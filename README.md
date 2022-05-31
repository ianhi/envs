# Ian's conda environments

Kept here for consistency across computers.

For non-vim versions use the `envs/no_vim` folder and add `no-vim` to the file name.

# Microscopy

**micro-base**
base env + napari + xarray + image loading

```bash
mamba env create --force --file https://raw.githubusercontent.com/ianhi/envs/main/envs/micro-base.yaml
```

**micro-analysis**
`micro-base` + scikit image and learn

```bash
mamba env create --force --file https://raw.githubusercontent.com/ianhi/envs/main/envs/micro-analysis.yaml
```

**micro-analysis**
`micro-base` plus Controlling microscopes with pymmcore-plus and napari-micromanager

```bash
mamba env create --force --file https://raw.githubusercontent.com/ianhi/envs/main/envs/micro-control.yaml
```
