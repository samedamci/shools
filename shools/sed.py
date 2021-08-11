from subprocess import run, PIPE


class SedException(Exception):
    def __init__(self, error: bytes) -> None:
        self.message = str(error, encoding="utf-8").replace("sed: -e ", "")
        super().__init__(self.message)


def sed(input_str: str, expression: str) -> str:
    cmd = run(
        ["sed", expression],
        input=bytes(input_str, encoding="utf-8"),
        stdout=PIPE,
        stderr=PIPE,
    )
    if cmd.returncode == 0:
        return str(cmd.stdout, encoding="utf-8")
    else:
        raise SedException(cmd.stderr)
