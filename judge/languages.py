from problem.models import ProblemIOMode


default_env = ["LANG=en_US.UTF-8", "LANGUAGE=en_US:en", "LC_ALL=en_US.UTF-8"]

_c_lang_config = {
    "template": """//PREPEND BEGIN
#include <stdio.h>
//PREPEND END

//TEMPLATE BEGIN
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//TEMPLATE END

//APPEND BEGIN
int main() {
  printf("%d", add(1, 2));
  return 0;
}
//APPEND END""",
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 10000,
        "max_memory": 512 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_c_lang_spj_compile = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 3000,
    "max_real_time": 10000,
    "max_memory": 512 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c11 {src_path} -lm -o {exe_path}"
}

_c_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_cpp_lang_config = {
    "template": """//PREPEND BEGIN
#include <iostream>
//PREPEND END

//TEMPLATE BEGIN
int add(int a, int b) {
  // Please fill this blank
  return ___________;
}
//TEMPLATE END

//APPEND BEGIN
int main() {
  std::cout << add(1, 2);
  return 0;
}
//APPEND END""",
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 10000,
        "max_real_time": 20000,
        "max_memory": 1024 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++17 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": {ProblemIOMode.standard: "c_cpp", ProblemIOMode.file: "c_cpp_file_io"},
        "env": default_env
    }
}

_cpp_lang_spj_compile = {
    "src_name": "spj-{spj_version}.cpp",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 10000,
    "max_real_time": 20000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++17 {src_path} -lm -o {exe_path}"
}

_cpp_lang_spj_config = {
    "exe_name": "spj-{spj_version}",
    "command": "{exe_path} {in_file_path} {user_out_file_path}",
    "seccomp_rule": "c_cpp"
}

_java_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_py3_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.py",
        "exe_name": "solution_e.py",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": 256 * 1024 * 1024,
        "compile_command": "/bin/cp {src_path} {exe_path}",
    },
    "run": {
        "command": "/usr/bin/python3 {exe_path}",
        "seccomp_rule": "general",
        "env": default_env
    }
}

_js_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.js",
        "exe_name": "solution_e.js",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": -1,
        "compile_command": "/bin/cp {src_path} {exe_path}",
    },
    "run": {
        "command": "/usr/bin/node {exe_path}",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_bf_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "solution.bf",
        "exe_name": "solution_e.bf",
        "max_cpu_time": 5000,
        "max_real_time": 10000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/bin/cp {src_path} {exe_path}",
    },
    "run": {
        "command": "/usr/bin/brainfuck/brainfuck.py {exe_path}",
        "seccomp_rule": None,
        "env": default_env
    }
}

_kotlin_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.kt",
        "exe_name": "Main",
        "max_cpu_time": -1,
        "max_real_time": 30000,
        "max_memory": -1,
        "compile_command": "/usr/bin/kotlinc {src_path} -d {exe_dir}"
    },
    "run": {
        "command": "/usr/bin/java -cp /usr/lib/kotlin/*:{exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true MainKt",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

_scala_lang_config = {
    "template": """//PREPEND BEGIN
//PREPEND END

//TEMPLATE BEGIN
//TEMPLATE END

//APPEND BEGIN
//APPEND END""",
    "compile": {
        "src_name": "Main.scala",
        "exe_name": "Main",
        "max_cpu_time": -1,
        "max_real_time": 30000,
        "max_memory": -1,
        "compile_command": "/usr/bin/scalac {src_path} -d {exe_dir} -encoding UTF8 -language:postfixOps"
    },
    "run": {
        "command": "/usr/bin/java -cp /usr/lib/scala/scala-library.jar:{exe_dir} -XX:MaxRAM={max_memory}k -Djava.security.manager -Dfile.encoding=UTF-8 "
                   "-Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "env": default_env,
        "memory_limit_check_only": 1
    }
}

languages = [
    {"config": _c_lang_config, "spj": {"compile": _c_lang_spj_compile, "config": _c_lang_spj_config},
     "name": "C", "description": "GCC 9.3.0", "content_type": "text/x-csrc"},
    {"config": _cpp_lang_config, "spj": {"compile": _cpp_lang_spj_compile, "config": _cpp_lang_spj_config},
     "name": "C++", "description": "G++ 9.3.0", "content_type": "text/x-c++src"},
    {"config": _java_lang_config, "name": "Java", "description": "OpenJDK 11.0.7", "content_type": "text/x-java"},
    {"config": _py3_lang_config, "name": "Python3", "description": "Python 3.8.2", "content_type": "text/x-python"},
    {"config": _js_lang_config, "name": "JavaScript", "description": "Node.js v12.18.2", "content_type": "text/javascript"},
    {"config": _kotlin_lang_config, "name": "Kotlin", "description": "Kotlin 1.3.50", "content_type": "text/x-kotlin"},
    {"config": _scala_lang_config, "name": "Scala", "description": "Scala 2.13.0", "content_type": "text/x-scala"},
    {"config": _bf_lang_config, "name": "brainfuck", "description": "An interesting language", "content_type": "text/x-brainfuck"}
]
