# Anaconda Installation Guide
-------------------------------------------------------------------------------

1. Download
Download the latest installer from https://www.anaconda.com/products/individual
Choose the Linux 64-bit (x86) Installer.
The name should be something similar to "Anaconda3-2021.11-Linux-x86_64.sh"

2. Install
Bash command line: sh (the .sh installer you just downloaded)
Example: sh Anaconda3-2021.11-Linux-x86_64.sh
Then answer all questions.
It is recommended that you accept all the defaults.

IMPORTANT: When the installer asks
"Do you wish the installer to initialize Anaconda3 by running conda init?"
you must answer "YES".
If you didn't, execute the following line:
~/anaconda3/condabin/conda init

3. Open a new terminal
Close the current terminal and open a new one.
You should see that the bash prompt has changed and now it displays "(base)".
Also, you can type "echo $PATH" and check that now the conda PATH comes first.

Note: You can optionally customize your bash prompt.
The configuration is stored in ~/.bashrc.
Look for the PS1 variable.


# Environment creation
-------------------------------------------------------------------------------

Create a new environment called "prj":
conda create -n prj

Switch to the newly created environment:
conda activate prj

Return to the base environment when done:
conda deactivate



# R and RStudio installation
-------------------------------------------------------------------------------

Install with: 
conda install -n prj -c r r
conda install -n prj -c r rstudio

IMPORTANT: Make sure to install first r before rstudio.
Otherwise the dependency resolution takes a very long time.

Call Rstudio with:
conda activate prj
rstudio

-------------------------------------------------------------------------------

