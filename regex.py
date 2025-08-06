import re

# Sample string
text = ("abc123XYZ_abc123XYZ_abc123XYZ_456defGHI_456defGHI_789ghiJKL_abc123XYZ_456defGHI_abc123XYZ_"
        "helloWORLD123_helloWORLD123_456defGHI_goodbye2025_goodbye2025_helloWORLD123_zzz999zzz_"
        "zzz999zzz_abc123XYZ_loremIPSUM42_loremIPSUM42_456defGHI_TEST123_test123_TEST123_test123_TEST123_")

# Pattern: 3 letters/digits (no -), 3 digits, 3 letters/digits (no -)
pattern = r"[a-zA-Z0-9]{3}\d{3}[a-zA-Z0-9]{3}"

matches = re.findall(pattern, text)


print(matches)
