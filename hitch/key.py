from commandlib import python_bin, Command, CommandError
from hitchrun import DIR, expected
from pathquery import pathq
import patoolib
import shutil

hugo_dir = DIR.gen / "hugo"


def install():
    """
    Set up hugo.
    """
    if hugo_dir.exists():
        hugo_dir.rmtree(ignore_errors=True)

    Command(
        "wget", 
        "https://github.com/gohugoio/hugo/releases/download/v0.31.1/hugo_0.31.1_Linux-64bit.tar.gz",
    ).in_dir(DIR.gen).run()

    DIR.gen.chdir()
    patoolib.extract_archive(DIR.gen/"hugo_0.31.1_Linux-64bit.tar.gz")
    DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar/").move(hugo_dir)
    DIR.gen.joinpath("hugo_0.31.1_Linux-64bit.tar.gz").remove()


@expected(CommandError)
def hugo(*args):
    """
    Run Hugo
    """
    Command(hugo_dir/"hugo").in_dir(DIR.project)(*args).run()


def test():
    """
    Build all docs for all projects and run a test hugo server.
    """
    hugo("serve")
