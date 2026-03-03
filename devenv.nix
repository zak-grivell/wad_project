{ pkgs, ... }:

{
  packages = with pkgs; [
    ruff
    uv
    ty
  ];
}
