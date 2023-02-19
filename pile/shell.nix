with import (fetchTarball https://github.com/NixOS/nixpkgs/archive/22.11.tar.gz) {};

#pkgs.mkShell {
#  name = "pile-env";
#  buildInputs = [ 
##    manim
#    jetbrains.pycharm-professional
#    python3
#    cairo
#];
#}
let pythonPackages = python39Packages;
in pkgs.mkShell rec {
  name = "impurePythonEnv";
  venvDir = "./env";
  nativeBuildInputs = [ pkg-config autoPatchelfHook ];
  buildInputs = [
    # A Python interpreter including the 'venv' module is required to bootstrap
    # the environment.
    pythonPackages.python

    # This execute some shell code to initialize a venv in $venvDir before
    # dropping into the shell
    #pythonPackages.venvShellHook

    cairo.dev
    cairo
    pango
    ffmpeg
    # required by fastecdsa
    gmp
    jetbrains.pycharm-professional
  ];

  shellHook = ''
  source ".venv/bin/activate"
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH
  '';

  # Run this command, only after creating the virtual environment
  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -r requirements.txt
  '';

  # Now we can execute any commands within the virtual environment.
  # This is optional and can be left out to run pip manually.
  postShellHook = ''
    # allow pip to install wheels
    unset SOURCE_DATE_EPOCH
  '';

}
