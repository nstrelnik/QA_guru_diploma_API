login_successfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"token": {"type": "string"}},
    "required": ["token"],
}


login_unsuccessfully = {
    "type": "object",
    'additionalProperties': False,
    "properties": {"error": {"type": "string"}},
    "required": ["error"],
}