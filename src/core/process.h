#pragma once

#include "core/common.h"

namespace hz {

struct ProcessOptions {
    std::string cwd;
    std::string input;
    int timeoutMs = -1;
    bool mergeStderr = false;
    std::vector<std::string> env;
    std::vector<std::string> unsetEnv;
};

struct ProcessResult {
    bool started = false;
    bool timedOut = false;
    int code = -1;
    std::string out, err;
};

ProcessResult runCapture(const std::vector<std::string>& argv, const ProcessOptions& opt = {});
ProcessResult runShell(const std::string& command, const ProcessOptions& opt = {});

void* spawnProcess(const std::vector<std::string>& argv);
bool processFinished(void* p, int waitMs, int& exitCode);
void endProcess(void* p, bool kill);

bool openWithSystem(const std::string& target);
int currentProcessId();

}
