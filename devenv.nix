{ pkgs, ... }:

{
  languages.python = {
    enable = true;

    lsp.package = pkgs.ty;

    uv.enable = true;
  };

  packages = with pkgs; [
    ruff
  ];
}
