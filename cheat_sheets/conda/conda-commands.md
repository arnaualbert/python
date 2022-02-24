# Conda Commands
-------------------------------------------------------------------------------

# Create a 'prj' environment
conda create  -n prj python=3.9
conda install -n prj -c conda-forge jupyterlab
conda install -n prj -c anaconda    pandas

# Install tools
conda install -y -n prj -c anaconda pylint
conda install -y -n prj -c conda-forge black
conda install -y -n prj -c conda-forge mypy
conda install -y -n prj -c conda-forge pytest

# Remove an environment
conda
conda env 
conda env list
conda env remove -n prj

# Remove conda
https://docs.anaconda.com/anaconda/install/uninstall/
cd
conda install anaconda-clean
anaconda-clean
rm -r ~/.anaconda_backup
rm -r ~/anaconda3
nano ~/.bash_rc  # Remove last conda init section
source ~/.bashrc # Or better close the terminal

-------------------------------------------------------------------------------

