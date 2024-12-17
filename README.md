# pysample

This project provides a basic setup for a Python environment within Visual Studio Code (VSCode).

## Environment Setup

To set up the Python environment in VSCode, follow these steps:

### For Run in terminal

1. Open the `.vscode/settings.json` file in the root of your project.
2. Add the following code to set the `PYTHONPATH` environment variable:

```json
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
```

### For Debugging

1. Open the .vscode/launch.json file in the root of your project.
2. Add the following code to configure the Python debugger:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "env": {
                "PYTHONPATH": "${workspaceFolder}/src"
            }
        }
    ]
}
```

## Usage

Once the environment is set up, you can run and debug your Python code within VSCode.