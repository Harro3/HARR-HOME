from setuptools import setup, find_packages

setup(
    name="harr_home",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["discord.py", "python-dotenv", "sense_emu", "sense_hat", "pgi", "pycairo", "pyGObject"]
)
