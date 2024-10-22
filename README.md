# pysample

Sample Python Project for VSCode Environments
This project provides a basic setup for a Python environment within Visual Studio Code (VSCode).

## Run in terminal
Modify .vscode/settings.json

    {
      "terminal.integrated.env.osx": {
        "PYTHONPATH": "${workspaceFolder}/src",
      },
      "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}/src",
      },
      "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}/src",
      }
    }

## Debugging

Modify .vscode/launch.json

    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python Debugger: Current File",
                "type": "debugpy",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "env": {"PYTHONPATH": "${workspaceFolder}/src"} // add this
            }
        ]
    }
