Clone this repository
====
    git clone git@github.com:Neurita/neurita.github.io.git
    git pull && git submodule update --init --recursive


Publish a Pelican site in the form of User Pages to Github
====

First, we run pelican locally.:

```bash
$ ./develop_server.sh start
$ firefox "localhost:8000"
```

Then, If we like the results, we publish the site to Github.:

```bash
$ ./develop_server.sh stop
$ ghp-import output
$ git push git@github.com:username/username.github.io.git gh-pages:master
```
