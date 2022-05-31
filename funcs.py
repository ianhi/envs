from __future__ import annotations
import yaml

def extend_env(base, env):
    base_conda = base.get("conda", [])
    base_pip = base.get("pip", [])
    conda = env.get("conda", [])
    pip = env.get("pip", [])
    conda.extend(base_conda)
    pip.extend(base_pip)
    return {"pip": list(sorted(set(pip))), "conda": list(sorted(set(conda)))}


# thanks to https://github.com/yaml/pyyaml/issues/234#issuecomment-765894586
class Dumper(yaml.Dumper):
    def increase_indent(self, flow=False, *args, **kwargs):
        return super().increase_indent(flow=flow, indentless=False)


def remove_vim(deps: list[str | dict]) -> list[str | dict]:
    out = []
    for d in deps:
        if isinstance(d, dict):
            dict_ = {}
            for k, v in d.items():
                dict_[k] = remove_vim(v)
            out.append(dict_)
        elif "vim" not in d:
            out.append(d)
    return out


def dump_env(env_dir, name, env, no_vim_dir=None):
    """take my garbo dict of env and put in the conda forge format

    Parameters
    ----------
    name : str
    env : dict
    no_vim : path
        If not None also generate a no_vim version without jupyterlab vim plugins
    """
    dependencies = env.get("conda", [])
    pip = env.get("pip", [])
    dependencies.append({"pip": pip})
    env = {"name": name, "channels": ["conda-forge"], "dependencies": dependencies}
    with open(env_dir / (name + ".yaml"), "w") as f:
        yaml.dump(env, f, Dumper=Dumper)
    if no_vim_dir is not None:
        vim_free = remove_vim(dependencies)
        env["dependencies"] = vim_free
        with open(no_vim_dir / (name + "-no-vim.yaml"), "w") as f:
            yaml.dump(env, f, Dumper=Dumper)
