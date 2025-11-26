{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
    ...
  } @ inputs: let
    systems = [
      "x86_64-linux"
    ];

    forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f pkgsFor.${system});

    pkgsFor = nixpkgs.lib.genAttrs systems (
      system:
        import nixpkgs {
          inherit system;
          config.allowUnfree = true;
        }
    );
  in {
    formatter = forAllSystems (pkgs: pkgs.alejandra);

    devShells = forAllSystems (
      pkgs: {
        default = let
          python = pkgs.python313.withPackages (ps:
            with ps; [
              tkinter
            ]);
        in
          pkgs.mkShell {
            buildInputs = with pkgs; [
              glibc_multi
              uv
              python
              tk
              tcl
            ];

            NIX_LD_LIBRARY_PATH = with pkgs;
              lib.makeLibraryPath [
                stdenv.cc.cc
                libz
              ];

            NIX_LD = builtins.readFile "${pkgs.stdenv.cc}/nix-support/dynamic-linker";

            shellHook = ''
              export LD_LIBRARY_PATH="$NIX_LD_LIBRARY_PATH"
              export PYTHONPATH="${python}/lib/python3.13/site-packages:$PYTHONPATH"
              export TCL_LIBRARY="${pkgs.tcl}/lib/tcl${pkgs.tcl.version}"
              export TK_LIBRARY="${pkgs.tk}/lib/tk${pkgs.tk.version}"
            '';
          };
      }
    );
  };
}
