from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src", pty=True)

#@task
#def lint(ctx):
#    ctx.run("pylint src", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)
    ctx.run("coverage report -m", pty=True)
    ctx.run("coverage html", pty=True)

@task
def clean(ctx): 
    """cleans up python files"""
    
    ctx.run("autopep8 --in-place --aggressive src/*.py", pty=True)
    ctx.run("autopep8 --in-place --aggressive src/*/*.py", pty=True)