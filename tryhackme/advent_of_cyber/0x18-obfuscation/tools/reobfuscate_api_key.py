# API Key Re-Obfuscation Tool
# Technique: Single-byte XOR with key 0x37
# Output: Hexadecimal string for PowerShell embedding



def xor_obfuscate(plaintext, key=0x37):
    return "".join(format(b ^ key, "02x") for b in plaintext.encode("utf-8"))


api_key = "CANDY-CANE-API-KEY"
obfuscated = xor_obfuscate(api_key)

print(f"Original: {api_key}")
print(f"Obfuscated (hex): {obfuscated}")
print("\nPowerShell Reconstruction:")
print(
    f'$ApiKey = [char[]]0x{",0x".join(obfuscated[i : i + 2] for i in range(0, len(obfuscated), 2))} -join ""'
)
