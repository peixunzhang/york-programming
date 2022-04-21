{

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-21.05-darwin";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:

    flake-utils.lib.simpleFlake {
      inherit self nixpkgs;

      name = "york";

      shell = { pkgs }:
        with pkgs;
        mkShell {
          packages = [
            (python37.withPackages (ps: with ps; [ tkinter pandas requests matplotlib scipy ]))
          ];
        };
    };
}
