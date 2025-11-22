def inc(n: int) -> int:
    return n + 1

def main() -> None:
    import pytest
    import sys
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    sys.path.insert(0, os.path.join(project_root, "src"))
    sys.exit(pytest.main([os.path.join(project_root, "tests")]))
