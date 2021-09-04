import os
import argparse

import package


def main(experiment, run_name):
    project_path = os.path.expanduser('~/package')
    base_dir = os.path.join(project_path, "experiments", experiment)
    params = package.utils.load_yaml(os.path.join(base_dir, 'hyperparams.yaml'))[run_name]
    run_dir = os.path.join(base_dir, run_name)

    if not os.path.exists(run_dir): os.makedirs(run_dir)
    
    model = package.instantiate(params, run_dir=run_dir)

    # TODO

        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='example script.')
    parser.add_argument('experiment', type=str, help='experiment')
    parser.add_argument('run_name', type=str, help='run_name')
    
    args = parser.parse_args()
    main(args.experiment, args.run_name)
