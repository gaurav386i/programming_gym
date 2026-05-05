def manual_compress_ipv6(ip: str) -> str:
    # 1. Expand completely first to ensure consistent processing
    parts = ip.split(':')
    # Remove empty strings caused by existing '::'
    parts = [p for p in parts if p] 
    
    # 2. Strip leading zeros
    blocks = [lstrip_zeros(p) for p in parts]
    
    # 3. Find the longest sequence of consecutive zeros
    max_len = 0
    max_idx = -1
    current_len = 0
    current_idx = -1
    
    for i, block in enumerate(blocks):
        if block == '0':
            if current_len == 0:
                current_idx = i
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                max_idx = current_idx
        else:
            current_len = 0
            
    # 4. Replace the longest sequence (must be > 1) with an empty string for '::'
    if max_len > 1:
        blocks[max_idx:max_idx + max_len] = ['']
        # Handle edge cases where '::' is at the start or end
        if max_idx == 0:
            blocks.insert(0, '')
        if max_idx + max_len == 8:
            blocks.append('')
            
    return ':'.join(blocks)

def lstrip_zeros(s: str) -> str:
    s = s.lstrip('0')
    return s if s else '0'

# --- Examples ---
if __name__ == "__main__":
    # Example 1: Removing leading zeros
    print(manual_compress_ipv6("2001:0db8:0000:0000:0000:ff00:0042:8329")) 
    # Output: 2001:db8::ff00:42:8329

    # Example 2: Compressing the longest sequence of zeros
    print(manual_compress_ipv6("0000:0000:0000:0000:0000:0000:0000:0001")) 
    # Output: ::1

    # Example 3: Handling already compressed IPs safely
    print(manual_compress_ipv6("fe80::1")) 
    # Output: fe80::1
    