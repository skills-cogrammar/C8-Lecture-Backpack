@echo off
REM Cloning the repository with sparse checkout
git clone --filter=blob:none --sparse https://github.com/HyperionDevBootcamps/2024-Commercial-Lecture-Backpack.git

REM Changing directory to the cloned repository
cd 2024-Commercial-Lecture-Backpack

REM Adding the specific folders to sparse checkout
git sparse-checkout add "Data Science (DS)"
git sparse-checkout add "StarterPack"

@echo on
