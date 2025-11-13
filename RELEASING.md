# Releasing the ea


```shell
cldfbench makecldf cldfbench_teow.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_teow.py
cldfbench zenodo --communities dplace cldfbench_teow.py
dplace check cldfbench_teow.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_teow.py vX.Y
```