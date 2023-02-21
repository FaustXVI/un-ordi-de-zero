with import (fetchTarball https://github.com/FaustXVI/nixpkgs/archive/manim-voiceover-0.17.tar.gz) {};

pkgs.mkShell {
  name = "pile-env";
  packages = [ 
    jetbrains.pycharm-professional
    (python3.withPackages (p: with p;[ manim-voiceover manim]))
];
}
