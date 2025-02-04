from setuptools import setup, find_packages

setup(
    name='babyai',
    version='0.1.0',
    license='BSD 3-clause',
    keywords='memory, environment, agent, rl, openaigym, openai-gym, gym',
    packages=find_packages(),
    # packages=['babyai', 'babyai.rl', 'babyai.levels', 'babyai.utils'],
    install_requires=[
        'gym>=0.9.6,<0.26.2',
        'numpy>=1.17.0',
        "torch>=0.4.1",
        'blosc>=1.5.1',
        "matplotlib>=3.7",
        "tqdm==4.65",
        # 'gym_minigrid @ https://github.com/maximecb/gym-minigrid/archive/master.zip'
    ],
)
