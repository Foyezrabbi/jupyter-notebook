import subprocess

try:
    open_jupyter_notebook = subprocess.Popen('jupyter notebook')
except Exception:
    from pip._internal import main as pip

    try:
        pip(['install', '--user', 'jupyter'])
    except Exception as e:
        print(e)
        pip(['install', 'jupyter'])
    try:

        open_jupyter_notebook = subprocess.Popen('jupyter notebook')
    except Exception:
        open_jupyter_notebook = subprocess.Popen('python -m notebook')
