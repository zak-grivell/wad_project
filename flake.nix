{
  description = "Python Template";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};

       reset_db = pkgs.writeShellScriptBin "django-db-reset" ''
          rm db.sqlite3
          rm -r concertainly/migrations

          uv run manage.py makemigrations concertainly
          uv run manage.py migrate
          uv run populate_concertainly.py     
       '';

        nativeBuildInputs = with pkgs; [
            uv
            ruff
            ty

            reset_db

            vscode-langservers-extracted
            typescript-language-server
        ];
        
        buildInputs = with pkgs; [];
      in {
        devShells.default = pkgs.mkShell {inherit nativeBuildInputs buildInputs;};
      }
    );
}
