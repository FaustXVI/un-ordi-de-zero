with import (fetchTarball https://github.com/FaustXVI/nixpkgs/archive/manim-voiceover-0.17.tar.gz) {};

pkgs.mkShell {
  name = "un-pas-apres-l-autre-env";
  packages = [
    sox
    jetbrains.pycharm-professional
    (python3.withPackages (p: with p;[ manim-voiceover manim pip ] 
    ++ manim-voiceover.optional-dependencies.recorder
    ++ manim-voiceover.optional-dependencies.transcribe
    ))
    texlive.combined.scheme-full
    gst_all_1.gstreamer
    intltool
    gobject-introspection
    gst_all_1.gst-plugins-base
    gst_all_1.gst-plugins-bad
    gst_all_1.gst-plugins-good
    gst_all_1.gst-plugins-ugly
];
}
