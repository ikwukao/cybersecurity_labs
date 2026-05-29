import json

# Generate CyberChef Recipe JSON
ops = [
    {"op": "From Base64", "args": ["A-Za-z0-9+/=", True, False]},
    {"op": "XOR", "args": [{"option": "UTF8", "string": "cyberchef"}, "Hex", False]},
]
print(json.dumps(ops, indent=2))
