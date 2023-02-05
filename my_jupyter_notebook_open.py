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
    open_jupyter_notebook = subprocess.Popen('jupyter notebook')
