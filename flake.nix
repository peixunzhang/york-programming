{

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-21.11";
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
            (python37.withPackages (ps: with ps; [ jupyterlab tkinter pandas requests matplotlib ]))

          ];
        };
    };
}
