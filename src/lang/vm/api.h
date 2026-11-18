#pragma once

#include "core/common.h"

namespace hz {

struct ApiParam {
    std::string name;
    std::string type = "any";
    std::string def;
    bool optional = false;
    bool rest = false;
};

enum class ApiKind : uint8_t { Function, Property, Method, Constant, Event, Class, Module, Field };

struct ApiEntry {
    ApiKind kind = ApiKind::Function;
    std::string owner;
    std::string name;
    std::vector<ApiParam> params;
    std::string returns = "void";
    std::string type;
    std::string doc;
    std::string example;
    bool readonly = false;
    bool isStatic = false;
    std::string status = "estable";
    int minArgs = 0, maxArgs = 0;
    std::string signature() const;
};

bool parseApiSignature(const std::string& sig, std::vector<ApiParam>& params, std::string& ret);

}
