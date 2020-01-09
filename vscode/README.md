
## json配置
对于编译c/c++工程，常用的几个配置：tasks.json，launch.json，setting.json
tasks.json是用来设置指令编译代码，launch.json是设置执行环境来执行代码。setting是设置语言环境

在当前文件是C++的情况下，tasks可以被用来做编译，而launch用来执行编译好的文件

说明：vs code官方文档没有提供linux下的配置说明，只有wsl（Windows Subsystem for Linux）的，但是道理都是相通的。

### tasks.json
告诉VS代码如何构建(编译)程序
示例配置和参数说明：
```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "label": "build",  // task的名字是build,在launch.json内根据此任务名调用此任务；
            "type": "shell",   // 任务执行的是shell命令
            "command": [ "vcvarsall.bat && gmake TARGET_PLATFORM=PC TARGET_BUILD=debug CORE=eve RUN_REF_FOR_STATS=1  all"],  // 执行的具体指令
            "args": [         // 如果上述的shell命令需要对象，则在这里添加，不需要可直接删掉；
                "'-Wall'",
                "'-std=c++17'",  //使用c++17标准编译
                "'${file}'", //当前文件名
                "-o", //对象名，不进行编译优化
                "'${fileBasenameNoExtension}.exe'",  //当前文件名（去掉扩展名）
            ],
            "problemMatcher": [
                "$msCompile"      //设置捕获错误的工具；
            ]
        }
    ]
```

### launch.json
配置VS Code以在按F5调试程序时在WSL上启动GDB
应该选 launch不选attach，attach用来给正在执行的文件用的，比如网页中的组件，而launch是执行新文件。
launch.json配置项解释:
```json
{
    {
        "version": "0.2.0",
        "configurations": [
            {
                "version": "0.2.0",
                "configurations": [],
                "compounds": []
            },
            {
                "name": "C++ Launch (GDB)",  // 配置名称，将会在启动配置的下拉菜单中显示
                "type": "cppdbg", // 配置类型，这里只能为cppdbg
                "request": "launch",  // 请求配置类型，可以为launch（启动）或attach（附加)
                "launchOptionType": "Local",  // 调试器启动类型，这里只能为Local
                "targetArchitecture": "x86", // 生成目标架构，一般为x86或x64, 可以为x86, arm, arm64, mips, x64, amd64, x86_64 
                "program": "${workspaceRoot}",  // 将要进行调试的程序的路径
                "miDebuggerPath":"D:\\mingw\\bin\\gdb.exe",  // miDebugger的路径，注意这里要与MinGw的路径对应
                "args": [],  // 程序调试时传递给程序的命令行参数，一般设为空即可 
                "stopAtEntry": false,  // 设为true时程序将暂停在程序入口处，一般设置为false
                "cwd": "${workspaceRoot}",  // 调试程序时的工作目录，一般为${workspaceRoot}即代码所在目录
                "externalConsole": true,  // 调试时是否显示控制台窗口，一般设置为true显示控制台
                "preLaunchTask": "g++"　　// 调试会话开始前执行的任务，一般为编译程序，c++为g++, c为gcc
            }
        ]
    }
}
```

### setting.json
示例：
```json
{
    "files.associations": {
        "tidl_alg_int.h": "c",
        "limits": "c"
    }
}
```

附：
1. [Visual Studio Code (vscode) 配置C、C++环境/编写运行C、C++（Windows](https://blog.csdn.net/bat67/article/details/81268581)
2. [如何优雅的用 VScode 编写 C++ 大型项目？](https://www.zhihu.com/question/353722203?sort=created)

