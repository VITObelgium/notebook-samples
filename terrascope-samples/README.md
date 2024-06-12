# Notebooks #

These notebooks run in the notebook environments of both Terrascope and PROBA-V MEP ([https://proba-v-mep.esa.int/notebooks](https://proba-v-mep.esa.int/notebooks)):

These samples are also available when you log in to the notebook environment, under: 'notebook-samples'.

## Updating ##
We make regular updates to these samples. To make sure everyone is using the latest version of the samples, they are updated automatically for every user on monday 2am. 

The update process is the following:
* Your local changes are being stashed (`git stash -U`)
* Next, new commits for repository and submodules get pulled with `git pull --rebase --recurse-submodules`.
* Finally, the submodules are updated to ensure that when a new submodule is added, the repository will also contain the new submodule. This is done with `git submodule update --init --recursive`.

To get your local changes back, you can execute `git stash pop`. This will put your local changes back, but it is possible you have some merge conflicts. 

## Disclaimer ##
This repository contains notebook samples that can run on Terrascope or PROBA-V MEP. All samples are provided AS-IS, and should not be assumed to be scientifically correct. 
