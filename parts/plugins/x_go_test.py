import os
from snapcraft.plugins.go import GoPlugin

class GoTestPlugin(GoPlugin):

    """
    def _remote_build(self):
        pass
    def clean_build(self):
        super().clean_build()
    """
    def build(self):
        install_bin_path = os.path.join(self.installdir, 'bin')
        os.makedirs(install_bin_path, exist_ok=True)
        self._run(['go', 'test', '-c', 'snapd/integration-tests/tests', '-test-build-tags=excludereboots,allsnaps', '-o', os.path.join(install_bin_path, 'snappy-tests')])
        return
"""
    def build(self):
        super().build()
        if self.options.source is not None:
            self._local_build()
        self._remote_build()

        install_bin_path = os.path.join(self.installdir, 'bin')
        os.makedirs(install_bin_path, exist_ok=True)
        os.makedirs(self._gopath_bin, exist_ok=True)
        for binary in os.listdir(os.path.join(self._gopath_bin)):
            binary_path = os.path.join(self._gopath_bin, binary)
            shutil.copy2(binary_path, install_bin_path)
"""
