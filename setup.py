from setuptools import setup


setup(
    name='cldfbench_teow',
    py_modules=['cldfbench_teow'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-teow=cldfbench_teow:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
