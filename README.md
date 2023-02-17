# Runtime templates

This repository contains runtime templates to build functions packages (a.k.a `rootfs`).

## What are function packages ?

Function packages, also called `rootfs`, are ready-to-use FS to start Firecracker microVM. The package includes all the following items :

- The function code
- The function wrapper
- All the function dependencies
- The underlying runtime to run the function (Node, Python, Go ...)

To build a function package, you should use the [morty](https://github.com/polyxia-org/morty) CLI. Please refer to the [morty's README](https://github.com/polyxia-org/runtimes/blob/main/README.md) for more details about how function packages are built.

## How to develop a template

> **At the moment, we support only languages that provide HTTP server through their standard library or external dependencies.**

To create a new template runtime, you must follow the following steps : 

- Create a folder into the `template` directory, for example : `template/node-19`
- Create the wrapper script with the embedded HTTP server. The wrapper HTTP server must expose import the function, and map it to all the routes / methods. See the example of [node-19](./template/node-19/index.js).
- Create a `Dockerfile` and a `.dockerignore` file. Check existing examples for how to structure these files.
