{ pkgs }: {
    deps = [
      pkgs.python39Packages.flask
      pkgs.qtile
        pkgs.cowsay
    ];
}