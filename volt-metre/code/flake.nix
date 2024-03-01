{
  description = "my project description";

  inputs = {
    nixpkgs.url = "github:FaustXVI/nixpkgs/manim-voiceover-0.17";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem
      (system:
      let pkgs = import nixpkgs {
        inherit system;
        config.allowUnfree = true;
      }; in
        {
          devShells.default = import ./shell.nix { inherit pkgs; };
        }
      );
}
