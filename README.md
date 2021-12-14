# rsc-pypi

run a `pypiserver` on RStudio Connect

## why

you need a way to serve python packages that you don't wish to push to PyPI

## how

`pypiserver` will let you invoke the [app method without starting a WSGI server](https://github.com/pypiserver/pypiserver#using-a-different-wsgi-server), making it perfect for a handoff to Connect.

## setup

1. create a `./packages` directory
1. create a test package in the directory with `poetry new <test-package>`
1. build the test package with `poetry build`
1. deploy the project directory with

    ```
    $ rsconnect deploy api . -n <SERVER-NICKNAME>
    ```

## limitations / to fix / extensions

i've attempted to set the server up for htpasswd access so packages can be deployed via the command line, but so far this doesn't work, so packages are being uploaded as part of the connect bundle
    - mostly this throws 405 errors, whether I use `poetry publish` or `twine`
    - [pypi-uploader](https://pypi.org/project/pypi-uploader/) may be an alternative to explore
    - perhaps more configuration of the built in bottle server is required
