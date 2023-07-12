import launch


def check_matplotlib():
    if not launch.is_installed("matplotlib"):
        return False

    try:
        import matplotlib
    except ImportError:
        return False

    if hasattr(matplotlib, "__version_info__"):
        version = matplotlib.__version_info__
        return version.major >= 3 and version.minor >= 6 and version.micro >= 2
    return False


if not check_matplotlib():
    launch.run_pip("install matplotlib==3.6.2", desc="Installing matplotlib==3.7.2")

launch.run_pip("pip install font-roboto", desc="installing roboto font")
