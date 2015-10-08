from setuptools import setup

setup(
    name='firetv',
    version='1.0.0',
    description='Communicate with an Amazon Fire TV device via ADB over a network.',
    license='MIT',
    packages=['firetv'],
    install_requires=['adb>=1.1.1'],
    extras_require={
        'firetv-server': ['Flask>=0.10.1']
    },
    entry_points={
        'console_scripts': [
            'firetv-server = firetv.__main__:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
    ]
)
