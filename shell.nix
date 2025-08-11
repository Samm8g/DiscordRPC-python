{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    python313Packages.pypresence    
    python313Packages.python-dotenv
  ];

  shellHook = ''
    python3 main.py
  '';
}
