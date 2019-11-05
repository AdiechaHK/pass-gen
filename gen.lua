#!/usr/bin/env resty

if not arg[1] then
  print("usage:   hash_basicauth.lua <password> [<uuid>]")
  print("example: hash_basicauth.lua abc123")
  os.exit(1)
end

local crypto = require "kong.plugins.basic-auth.crypto"
local utils = require "kong.tools.utils"

local id = arg[2] or utils.uuid()
print("consumer uuid: " .. id)
print("password hash: " .. crypto.hash(id, arg[1]))
