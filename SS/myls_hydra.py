
import hydra
from omegaconf import DictConfig, OmegaConf
from myls import myls


@hydra.main(version_base=None, config_path=".", config_name="myls_config.yaml")
def main(cfg : DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    
    targets = cfg.targets
    all_files = cfg.all
    long_format = cfg.long
    verbose = cfg.verbose
    recursive = cfg.recursive
    human_readable = cfg.human_readable
    
    myls(targets, all_files, long_format, verbose, recursive, human_readable)
    
if __name__ == "__main__":
    main()
